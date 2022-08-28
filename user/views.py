from .models import User
from .serializers import UserSerializerForCreateClient, UserSerializerForCreateStaff
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .permissions import OwnProfilePermission
from rest_framework import viewsets

# Creating ViewSet for clients
class ClientViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff = False)
    serializer_class = UserSerializerForCreateClient

    def get_permissions(self):
        # Anyone can create a client account, only owner can edit it.
        if self.action == "create":
            self.permission_classes = [AllowAny]
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAuthenticated, OwnProfilePermission]
            return [permission() for permission in self.permission_classes]


# Creating ViewSet for employes
class StaffViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerForCreateStaff

    def get_permissions(self):
        # Only staff or admin can create a staff account, only owner can edit it.
        if self.action == "create":
            self.permission_classes = [IsAdminUser]
            return [permission() for permission in self.permission_classes]
        else:
            self.permission_classes = [IsAuthenticated, OwnProfilePermission]
            return [permission() for permission in self.permission_classes]