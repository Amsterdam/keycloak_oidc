from rest_framework.permissions import BasePermission


class InAuthGroup(BasePermission):
    allowed_group_names = None

    def __init__(self):
        if self.allowed_group_names is None:
            raise Exception("Allowed group names must be set when using the AuthGroupPermission class")

        super().__init__()

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated
                    and request.user.groups.filter(name__in=self.allowed_group_names).exists())
