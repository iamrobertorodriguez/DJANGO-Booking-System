from rest_framework import viewsets
from .models import Reservation
from room.models import Room
from .serializers import ReservationSerializer, ReservationSerializerForCreate, ReservationSerializerForUpdate
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_permissions(self):
        # Any client can make a reservation
        if self.action == "create":
            self.permission_classes = [IsAuthenticated]
            return [permission() for permission in self.permission_classes]
        # Only employes can edit it
        else:
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]

    # Re-defining reservation creation
    def create(self, request, *args, **kwargs):

        # Defining serialize to use
        self.serializer_class = ReservationSerializerForCreate

        # Accessing to request body as a dictionary
        body = json.loads(request.body.decode())

        # Only account owner or staff in name of account owner can make reservations for this account
        if request.user.id!=body['user']:
            if request.user.is_staff:
                pass
            else:
                return JsonResponse({
                    "detail": "Only account owner or staff in name of account owner can make reservations for this account"
                }, status=status.HTTP_403_FORBIDDEN)

        # Getting room
        room = Room.objects.get(pk=body['room'])

        # Checking if room is available
        if not room.is_available:
            return JsonResponse({
                    "detail": "The choosed room is not available, try another one"
                }, status=status.HTTP_406_NOT_ACCEPTABLE)

        # Calculating total price
        request.data.update({'total_price': f"${float(room.price_per_night) * body['days_of_stay']} {room.currency}"}) 

        # Performing creation
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Setting room as occupated
        room.is_available = False
        room.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Re-defining reservation update
    def update(self, request, pk, *args, **kwargs):

        # Defining serialize to use
        self.serializer_class = ReservationSerializerForUpdate

        # Accessing to request body as a dictionary
        body = json.loads(request.body.decode())

        # If reservation is ending (status: 'RMVD') then set room available again
        if body['status'] and body['status'] == 'RMVD':
            reservation = Reservation.objects.get(pk=pk)
            room = Room.objects.get(pk=reservation.room.id)
            room.is_available = True
            room.save()

        # Performing reservation update
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)