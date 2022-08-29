from rest_framework import serializers
from .models import Reservation
from user.serializers import UserSerializer
from room.serializers import RoomSerializer
from django.utils.translation import gettext_lazy as _

class ReservationSerializer(serializers.ModelSerializer):

    # Adding user and room info for billing.
    user = UserSerializer(
        _("User ID"),
        help_text=_(
            "In this field only pass user ID"
        ),
    )
    room = RoomSerializer(
        _("Room ID"),
        help_text=_(
            "In this field only pass room ID"
        ),
    )

    class Meta:
        model = Reservation
        fields = '__all__'

class ReservationSerializerForCreate(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'payment_method',
            'days_of_stay',
            'total_price',
            'room',
            'user',
        ]

class ReservationSerializerForUpdate(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = [
            'payment_method',
            'days_of_stay',
            'total_price',
            'status',
            'room',
            'user',
        ]