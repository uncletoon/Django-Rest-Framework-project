from rest_framework import permissions
from .permissions import IsStaffEditorPermission

from django.db.models import Q
from products.models import Product

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

class UserQuerySetMixin():
    user_field = 'user'
    allow_admin_view = True

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_admin_view and user.is_superuser:
            return qs
        return qs.filter(**lookup_data)
