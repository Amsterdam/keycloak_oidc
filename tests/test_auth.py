from unittest import mock

from django.contrib.auth.models import Group, User
from django.test import TestCase
from model_mommy import mommy

from keycloak_oidc.auth import OIDCAuthenticationBackend


class TestAuth(TestCase):

    def test_create_user(self):
        claims = {
            'email': 'user@domain.com',
            'given_name': 'Firstname',
            'family_name': 'Lastname',
            'roles': ['testrole']
        }
        OIDCAuthenticationBackend().create_user(claims)

        self.assertTrue(
            User.objects.filter(
                email='user@domain.com',
                first_name='Firstname',
                last_name='Lastname',
                groups__name='testrole').exists(),
            "Expected user to be created with specific info")

    def test_update_user(self):
        user = mommy.make(User)
        original_email = user.email

        claims = {
            'email': 'user@domain.com',
            'given_name': 'Firstname',
            'family_name': 'Lastname',
            'roles': ['testrole']
        }
        OIDCAuthenticationBackend().update_user(user, claims)

        self.assertEqual(user.first_name, "Firstname", "Expected firstname to be updated")
        self.assertEqual(user.last_name, "Lastname", "Expected lastname to be updated")
        self.assertEqual(user.email, original_email, "Expected email not to be updated")
        self.assertTrue(user.groups.filter(name="testrole").exists(), "Expected new group to be added during update")

    def test_update_groups(self):
        user = mommy.make(User)
        group = Group.objects.create(name='old_group')
        group.user_set.add(user)

        claims = {'roles': ['new_group']}
        OIDCAuthenticationBackend().update_user(user, claims)

        self.assertTrue(user.groups.filter(name="new_group").exists(), "Expected new group to be added during update")
        self.assertFalse(user.groups.filter(name="old_group").exists(), "Expected old group to be added during update")

    @mock.patch('mozilla_django_oidc.auth.OIDCAuthenticationBackend.get_userinfo')
    @mock.patch('mozilla_django_oidc.auth.OIDCAuthenticationBackend.verify_token')
    def test_get_userinfo(self, mocked_verify_token, mocked_get_userinfo):
        mocked_get_userinfo.return_value = {}
        mocked_verify_token.return_value = {
            'realm_access': {
                'roles': [
                    'role1',
                    'role2'
                ]
            }
        }

        oidc_auth_backend = OIDCAuthenticationBackend()
        userinfo = oidc_auth_backend.get_userinfo(access_token="", id_token="", payload={})
        self.assertEqual(userinfo.get('roles'), ['role1', 'role2'], "Unexpected roles returned in get_userinfo")
