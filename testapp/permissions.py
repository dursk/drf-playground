from rest_framework.permissions import BasePermission


class Permission1(BasePermission):

    def has_permission(self, request, view):
        print 'In Permission1'
        return True


class Permission2(BasePermission):

    def has_permission(self, request, view):
        print 'In Permission2'
        return True
