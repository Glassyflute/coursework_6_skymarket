from rest_framework.permissions import BasePermission

from users.managers import UserRoles


class IsObjectAuthorOrStaff(BasePermission):
    message = "Вы не имеете доступа к этому объекту."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [UserRoles.ADMIN]:
            return True
        return False

