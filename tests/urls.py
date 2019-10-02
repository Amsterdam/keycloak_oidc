from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^oidc/', include('keycloak_oidc.urls')),
]
