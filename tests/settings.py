import os

from keycloak_oidc.default_settings import *  # noqa

SECRET_KEY = 'testing'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'keycloak_oidc',

    'rest_framework'    # used to test InAuthGroup permission
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'mozilla_django_oidc.middleware.SessionRefresh',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tests.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = '/tmp/'

AUTHENTICATION_BACKENDS = [
    'keycloak_oidc.auth.OIDCAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend'
]

OIDC_RP_CLIENT_ID = 'test'
OIDC_RP_CLIENT_SECRET = 'test'

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
