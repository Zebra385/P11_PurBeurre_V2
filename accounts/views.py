from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.views.generic.base import View

# Create your views here.


class LoginView(View):
    """
    That class to login a user of the site
    who are in the data base user admin
    """

    template_name = 'registration/login.html'


class LogoutView(View):
    """ That class to login out a user of site"""

    def post(self, request):
        print('je vais me logout')
        logout(request)
        # Redirect to a accueil page.
        return HttpResponseRedirect('/')
