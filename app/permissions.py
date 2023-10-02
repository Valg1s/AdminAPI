from rest_framework import permissions


class TokenRequiredPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated