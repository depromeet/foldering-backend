from rest_framework import permissions

class IsAuthorOrCantDelete(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return obj.author == request.user
        return True
        
