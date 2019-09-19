

# Keycloak OIDC

Keycloak OIDC is a simple Django app that wraps the mozilla_django_oidc 
app and implements Keycloak authentication the way we use it at Datapunt. 

It creates and updates users and sets their email, username and first- 
and lastname based on the info provided by keycloak, and manages
group membership based on keycloak roles.

## Quick start

1. Add "keycloak-oidc" to your INSTALLED_APPS (make sure to load after auth!):

    ```python
    INSTALLED_APPS = [
        ...
        'django.contrib.auth',
        'keycloak_oidc',  # load after auth!
    ]
    ```

2. Add the mozilla_django_oidc.SessionRefreshMiddleware to your MIDDLEWARE 
   (middleware involving session and authentication must come first!):

    ```python
    MIDDLEWARE = [
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'mozilla_django_oidc.middleware.SessionRefresh',
    ]
    ```

3. Add the OIDCAuthenticationBackend to the AUTHENTICATION_BACKENDS:

    ```python
    AUTHENTICATION_BACKENDS = [
        'keycloak_oidc.auth.OIDCAuthenticationBackend',
        ...
    ]
    ```

4. In settings.py import the default OIDC settings. These
   defaults will look at the OS env, or otherwise use sane
   defaults where possible. Make sure to set the OIDC_RP_CLIENT_ID
   and OIDC_RP_CLIENT_SECRET values in the OS environment. 
   These values need to be obtained from keycloak.

    ```python
    # Import from keycloak_oidc settings and use the defaults
    from keycloak_oidc.default_settings import *
    ```

5. Include the keycloak-oidc URLconf in your project urls.py:

    ```python
    url(r'^oidc/', include('keycloak_oidc.urls')),
    ```

6. Set the OIDC_RP_CLIENT_ID and OIDC_RP_CLIENT_SECRET. Note that
   these should be kept secret. Therefore these should preferable
   be set in the OS ENV. Obtain these from the keycloak provider.
    
7. When using Django-rest-framework, add the mozilla_django_oidc
   OIDCAuthentication to the default authentication classes:

    ```python
    REST_FRAMEWORK = dict(
        ...
        DEFAULT_AUTHENTICATION_CLASSES=(
            'mozilla_django_oidc.contrib.drf.OIDCAuthentication',
            ...
        )
    )
    ```

8. When using Django-rest-framework, override the InAuthGroup permission
   class to implement role based access control:

    ```python
    from keycloak_oidc.drf.permissions import InAuthGroup
    
    class InTestAuthGroup(InAuthGroup):
        """
        A permission to allow access if and only if a user is logged in,
        and is a member of the 'test' role inside keycloak.
        """
        allowed_group_names = ['test']
    ```

9. IMPORTANT: Make sure to read through the Mozilla Django OIDC docs:
   https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html
