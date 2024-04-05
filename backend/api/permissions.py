from rest_framework.permissions import BasePermission


class ClientPermissions(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user
