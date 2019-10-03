

# Keycloak OIDC

Keycloak OIDC is a simple Django app that wraps the mozilla_django_oidc 
app and implements Keycloak authentication the way we use it at Datapunt. 

It creates and updates users and sets their email, username and first- 
and lastname based on the info provided by keycloak, and manages
group membership based on keycloak roles.

## Quick start

1. Install using pip

    ```bash
    pip install datapunt_keycloak_oidc
    ```
   
2. Add "keycloak-oidc" to your INSTALLED_APPS (make sure to load after auth!):

    ```python
    INSTALLED_APPS = [
        ...
        'django.contrib.auth',
        'keycloak_oidc',  # load after auth!
    ]
    ```

3. Add the mozilla_django_oidc.SessionRefreshMiddleware to your MIDDLEWARE 
   (middleware involving session and authentication must come first!):

    ```python
    MIDDLEWARE = [
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'mozilla_django_oidc.middleware.SessionRefresh',
    ]
    ```

4. Add the OIDCAuthenticationBackend to the AUTHENTICATION_BACKENDS:

    ```python
    AUTHENTICATION_BACKENDS = [
        'keycloak_oidc.auth.OIDCAuthenticationBackend',
        ...
    ]
    ```

5. Set the OIDC_RP_CLIENT_ID and OIDC_RP_CLIENT_SECRET in settings.py. 
   Note that these should be kept secret. Therefore these should preferable
   be set in the OS ENV. Obtain these from the keycloak provider.

    ```python
    OIDC_RP_CLIENT_ID = os.environ['OIDC_RP_CLIENT_ID']
    OIDC_RP_CLIENT_SECRET = os.environ['OIDC_RP_CLIENT_SECRET']
    ```
   
   Keycloak only talks to urls that are whitelisted. Therefore, make
   sure that the app url for production is added to keycloak. To make
   local development possible, also make sure localhost:8080 (or any other port)
   is added. 
   
6. Add the OIDC provider URLs to settings.py, and set the proper OS env. This default
   will fall back to the acceptance keycloak urls.

    ```python
    OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv('OIDC_OP_AUTHORIZATION_ENDPOINT',
        'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/auth')
    OIDC_OP_TOKEN_ENDPOINT = os.getenv('OIDC_OP_TOKEN_ENDPOINT',
        'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/token')
    OIDC_OP_USER_ENDPOINT = os.getenv('OIDC_OP_USER_ENDPOINT',
        'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/userinfo')
    OIDC_OP_JWKS_ENDPOINT = os.getenv('OIDC_OP_JWKS_ENDPOINT',
        'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/certs')
    OIDC_OP_LOGOUT_ENDPOINT = os.getenv('OIDC_OP_LOGOUT_ENDPOINT',
        'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/logout')
    ```
   
7. When using Django-rest-framework, add the mozilla_django_oidc
   OIDCAuthentication to the default authentication classes (and
   make sure the DRF SessionAuthentication has been added):

    ```python
    REST_FRAMEWORK = dict(
        ...
        DEFAULT_AUTHENTICATION_CLASSES=(
            'mozilla_django_oidc.contrib.drf.OIDCAuthentication',
            'rest_framework.authentication.SessionAuthentication'
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
   
9. Include the keycloak-oidc URLconf in your project urls.py:

    ```python
    url(r'^oidc/', include('keycloak_oidc.urls')),
    ```

10. IMPORTANT: Make sure to read through the Mozilla Django OIDC docs:
   https://mozilla-django-oidc.readthedocs.io/en/stable/installation.html
   
   All settings that can be configured are documented there.
