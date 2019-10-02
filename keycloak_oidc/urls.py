from django.conf.urls import url
from django.urls import include

from keycloak_oidc.views import OIDCLogoutView

urlpatterns = [
    # Change logout url, allow GET
    url(r'^logout/$', OIDCLogoutView.as_view(), name='oidc_logout'),
    url(r'^', include('mozilla_django_oidc.urls')),

]
