from unittest import mock

from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse


class TestViews(TestCase):

    @mock.patch('keycloak_oidc.views.OIDCLogoutView.post')
    def test_get_userinfo(self, mocked_post):
        mocked_post.return_value = HttpResponse()
        self.client.get(reverse('oidc_logout'))
        mocked_post.assert_called()
