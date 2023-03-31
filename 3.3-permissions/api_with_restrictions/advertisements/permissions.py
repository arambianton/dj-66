from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed   

class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PATCH', 'DELETE']:
            return request.user.is_authenticated
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE']:
            boole = obj.creator == request.user
            if boole is True:
                return True
            else:
                raise(AuthenticationFailed('You can`t change or delete other person`s order'))
        return True