from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSelfOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # if request.method in SAFE_METHODS:
        #     return True

        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS:
        #     return True
        print(obj,request.user)
        return obj.username == request.user

