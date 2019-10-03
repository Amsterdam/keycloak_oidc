from django.apps import AppConfig
from django.conf import settings

from . import default_settings as defaults


class KeycloakOIDCConfig(AppConfig):
    name = 'keycloak_oidc'

    def ready(self):
        # Here we inject settings defined in default_settings. We can not use the
        # classic app_settings architecture with getattr(settings, 'SETTINGS_NAME', default),
        # because the defaults are not used by our app, but by mozilla django oidc.
        # Therefore we need to inject them.
        for name in dir(defaults):
            if name.isupper() and not hasattr(settings, name):
                setattr(settings, name, getattr(defaults, name))
