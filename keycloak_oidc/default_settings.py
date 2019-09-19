import os

OIDC_RP_CLIENT_ID = os.getenv('OIDC_RP_CLIENT_ID')
OIDC_RP_CLIENT_SECRET = os.getenv('OIDC_RP_CLIENT_SECRET')

OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv(
    'OIDC_OP_AUTHORIZATION_ENDPOINT', 'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/auth')
OIDC_OP_TOKEN_ENDPOINT = os.getenv(
    'OIDC_OP_TOKEN_ENDPOINT', 'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/token')
OIDC_OP_USER_ENDPOINT = os.getenv(
    'OIDC_OP_USER_ENDPOINT', 'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/userinfo')
OIDC_OP_JWKS_ENDPOINT = os.getenv(
    'OIDC_OP_JWKS_ENDPOINT', 'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/certs')
OIDC_OP_LOGOUT_ENDPOINT = os.getenv(
    'OIDC_OP_LOGOUT_ENDPOINT', 'https://iam.amsterdam.nl/auth/realms/datapunt-acc/protocol/openid-connect/logout')

OIDC_OP_LOGOUT_URL_METHOD = 'keycloak_oidc.utils.oidc_op_logout'
OIDC_USERNAME_ALGO = 'keycloak_oidc.utils.generate_username'
OIDC_RP_SIGN_ALGO = 'RS256'
OIDC_RP_SCOPES = 'openid email'

LOGIN_URL = 'oidc_authentication_init'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
