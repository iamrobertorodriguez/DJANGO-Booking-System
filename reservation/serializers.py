from dataclasses import fields
from rest_framework import serializers
from .models import Reservation
from user.serializers import UserSerializerForCreateClient
from room.serializers import RoomSerializer

class ReservationSerializer(serializers.ModelSerializer):

    # Adding user and room info for billing.
    user = UserSerializerForCreateClient()
    room = RoomSerializer()

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