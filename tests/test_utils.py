from django.test import RequestFactory, TestCase

from keycloak_oidc import utils


class TestUtils(TestCase):

    def test_generate_username_length(self):
        long_email = "{}@{}.com".format(
            "thisemailis22charslong" * 5,
            "thispartis21charslong" * 5
        )

        generated_username = utils.generate_username(long_email)
        self.assertEqual(len(generated_username), 150,
                         "Expected the generated username to be 150 chars")

    def test_oid_op_logout(self):
        request_factory = RequestFactory()
        request = request_factory.get('/')
        logout_redirect_url = "logout_redirect_url"
        oidc_logout_endpoint = "oidc_logout_endpoint"

        with self.settings(OIDC_OP_LOGOUT_ENDPOINT=oidc_logout_endpoint, LOGOUT_REDIRECT_URL=logout_redirect_url):
            logout_url = utils.oidc_op_logout(request)
            redirect_url = request.build_absolute_uri(logout_redirect_url)
            expected_logout_url = f"{oidc_logout_endpoint}?redirect_uri={redirect_url}"
            self.assertEqual(logout_url, expected_logout_url, "Generated OIDC logout url is unexpected")
