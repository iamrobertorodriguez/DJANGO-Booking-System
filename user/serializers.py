from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

# Standard user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'phone',
            'tax',
            'address',
        ]

# Making a serializer for managing clients accounts
class UserSerializerForCreateClient(serializers.ModelSerializer):

    # Hashing user password
    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        return super(UserSerializerForCreateClient, self).create(validate_data)

    class Meta:
        model = User
        fields = [
            'id',
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password',
            'phone',
            'tax',
            'address',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

# Making a serializer for managing employes accounts
class UserSerializerForCreateStaff(serializers.ModelSerializer):

    # Hashing user password
    def create(self, validate_data):
        validate_data['password'] = make_password(validate_data['password'])
        return super(UserSerializerForCreateStaff, self).create(validate_data)

    class Meta:
        model = User
        fields = [
            'id',
            'is_staff',
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password',
            'phone',
            'tax',
            'address',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }