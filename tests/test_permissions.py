from django.contrib.auth.models import Group, User
from django.http import HttpRequest
from django.test import TestCase
from model_mommy import mommy

from keycloak_oidc.drf.permissions import InAuthGroup


class InvalidTestPermission(InAuthGroup):
    pass


class ValidTestPermission(InAuthGroup):
    allowed_group_names = 'test'


class TestPermissions(TestCase):

    def test_missing_allow_group_names(self):
        self.assertRaises(Exception, InAuthGroup)
        self.assertRaises(Exception, InvalidTestPermission)

    def test_has_permission(self):
        permission = ValidTestPermission()

        group, _ = Group.objects.get_or_create(name='test')
        user = mommy.make(User)
        group.user_set.add(user)

        request = HttpRequest()
        request.user = user
        permission.has_permission(request, None)
