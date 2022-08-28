from rest_framework import permissions

# Creating permission for 'only owner' access.
class OwnProfilePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj == request.user