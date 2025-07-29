from rest_framework.permissions import BasePermission ,SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'

class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'user'

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only methods for everyone
        if request.method in SAFE_METHODS:
            return True

        # Write/delete permissions only to the owner (creator)
        # Assumes your model has a `user` ForeignKey pointing to creator
        return obj.user == request.user