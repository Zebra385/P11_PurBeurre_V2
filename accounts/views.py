from store.forms import CreatUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.views.generic.base import View
from django.views.generic.base import TemplateView

# Create your views here.


class LoginView(View):
    """
    That class to login a user of the site
    who are in the data base user admin
    """
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = '/'
        return context


class LogoutView(View):
    """ That class to login out a user of site"""

    def post(self, request):
        print('je vais me logout')
        logout(request)
        # Redirect to a accueil page.
        return HttpResponseRedirect('/')

class RegistrationView(View):
    

    def post(self, request):
        form = CreatUserForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                login((request, user))
                return HttpResponseRedirect("/")
        else:
            form = CreateUserForm()
            context = {'form': form, 'next': request.GET.get ('next', '')}
            return render(request, 'registration/register.html', context)

class InscriptionView(TemplateView):
    
    template_name= 'registration/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreatUserForm
        return context