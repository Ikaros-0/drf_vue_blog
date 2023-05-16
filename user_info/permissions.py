from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSelfOrReadOnly(BasePermission):
    """等待完善12:41 4/06"""
    # def has_object_permission(self, request, view, obj):
    #     if request.method in SAFE_METHODS:
    #         return True

    #     return obj == request.user

    """一轮完善12:58 4/06"""
    """log:增加了必须预先登录？"""
    def safe_methods_or_owner(self, request, func):
        if request.method in SAFE_METHODS:
            return True

        return func()

    # def has_permission(self, request, view):
    #     return self.safe_methods_or_owner(
    #         request,
    #         lambda: request.user.is_authenticated
    #     )

    def has_object_permission(self, request, view, obj):
        return self.safe_methods_or_owner(
            request,
            lambda: obj == request.user
        )