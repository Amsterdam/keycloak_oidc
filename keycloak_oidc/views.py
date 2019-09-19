from mozilla_django_oidc import views


class OIDCLogoutView(views.OIDCLogoutView):

    def get(self, request):
        """
        The OIDCLogoutView only implements logout via a post request, but we want a get request.
        Therefore allow that here
        """
        return self.post(request)
