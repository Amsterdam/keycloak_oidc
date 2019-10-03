from django.conf import settings
from django.test import TestCase


class TestSettings(TestCase):

    def test_injected_settings(self):
        # test that our default settings have been injected into the global settings
        self.assertEqual(settings.OIDC_OP_LOGOUT_URL_METHOD, 'keycloak_oidc.utils.oidc_op_logout',
                         f'Expected "OIDC_OP_LOGOUT_URL_METHOD" to be injected into settings')
        self.assertEqual(settings.OIDC_USERNAME_ALGO, 'keycloak_oidc.utils.generate_username',
                         f'Expected "OIDC_USERNAME_ALGO" to be injected into settings')
        self.assertEqual(settings.OIDC_RP_SIGN_ALGO, 'RS256',
                         f'Expected "OIDC_RP_SIGN_ALGO" to be injected into settings')
        self.assertEqual(settings.OIDC_RP_SCOPES, 'openid email',
                         f'Expected "OIDC_RP_SCOPES" to be injected into settings')

        self.assertEqual(settings.LOGIN_URL, 'oidc_authentication_init',
                         f'Expected "LOGIN_URL" to be injected into settings')
        self.assertEqual(settings.LOGIN_REDIRECT_URL, '/',
                         f'Expected "LOGIN_REDIRECT_URL" to be injected into settings')

        # test that the 'client' settings (in tests/settings.py) are properly loaded
        self.assertEqual(settings.OIDC_RP_CLIENT_ID, "test")
        self.assertEqual(settings.OIDC_RP_CLIENT_SECRET, "test")

        # test that the 'client' settings properly override the defailts
        self.assertEqual(settings.LOGOUT_REDIRECT_URL, 'test',
                         f'Expected "LOGOUT_REDIRECT_URL" to be injected into settings')
