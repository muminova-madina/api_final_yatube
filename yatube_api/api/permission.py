from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Доступ только для автора.'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
