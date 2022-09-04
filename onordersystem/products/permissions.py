from email import message
from rest_framework import permissions
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
  
class IsAdmin(permissions.BasePermission):
    message = 'Access this is only for super and staff users'
    def has_permission(self, request, view):
        return request.User.is_authenticated and (request.User.is_staff or request.User.is_superuser)



   
    
      

