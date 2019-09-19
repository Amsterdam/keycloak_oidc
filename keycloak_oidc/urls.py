from django.conf.urls import url
from django.urls import include

from keycloak_oidc.views import OIDCLogoutView

urlpatterns = [
    # Change logout url, allow GET
    url(r'^oidc/logout/', OIDCLogoutView.as_view(), name='oidc_logout'),
    url(r'^oidc/', include('mozilla_django_oidc.urls')),
]
