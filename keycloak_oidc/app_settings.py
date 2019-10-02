from django.conf import settings

OIDC_OP_AUTHORIZATION_ENDPOINT = getattr(
    settings, 'OIDC_OP_AUTHORIZATION_ENDPOINT',
    'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/auth')

OIDC_OP_TOKEN_ENDPOINT = getattr(
    settings, 'OIDC_OP_TOKEN_ENDPOINT',
    'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/token')

OIDC_OP_USER_ENDPOINT = getattr(
    settings,  'OIDC_OP_USER_ENDPOINT',
    'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/userinfo')

OIDC_OP_JWKS_ENDPOINT = getattr(
    settings,  'OIDC_OP_JWKS_ENDPOINT',
    'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/certs')

OIDC_OP_LOGOUT_ENDPOINT = getattr(
    settings, 'OIDC_OP_LOGOUT_ENDPOINT',
    'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/logout')

OIDC_OP_LOGOUT_URL_METHOD = getattr(settings, 'OIDC_OP_LOGOUT_URL_METHOD', 'keycloak_oidc.utils.oidc_op_logout')
OIDC_USERNAME_ALGO = getattr(settings, 'OIDC_USERNAME_ALGO', 'keycloak_oidc.utils.generate_username')
OIDC_RP_SIGN_ALGO = getattr(settings, 'OIDC_RP_SIGN_ALGO', 'RS256')
OIDC_RP_SCOPES = getattr(settings, 'OIDC_RP_SCOPES', 'openid email')

LOGIN_URL = getattr(settings, 'LOGIN_URL', 'oidc_authentication_init')
LOGIN_REDIRECT_URL = getattr(settings, 'LOGIN_REDIRECT_URL', '/')
LOGOUT_REDIRECT_URL = getattr(settings, 'LOGOUT_REDIRECT_URL', '/')
