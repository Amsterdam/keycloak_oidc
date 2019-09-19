import unicodedata

from django.conf import settings


def generate_username(email):
    # Using Python 3 and Django 1.11, usernames can contain alphanumeric
    # (ascii and unicode), _, @, +, . and - characters. So we normalize
    # it and slice at 150 characters.
    return unicodedata.normalize('NFKC', email)[:150]


def oidc_op_logout(request):
    oidc_op_logout_endpoint = settings.OIDC_OP_LOGOUT_ENDPOINT
    redirect_url = request.build_absolute_uri(getattr(settings, 'LOGOUT_REDIRECT_URL', '/'))
    return '{}?redirect_uri={}'.format(oidc_op_logout_endpoint, redirect_url)
