from accounts.forms import CreatUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from accounts.forms import CreatUserForm
# Create your views here.


class LoginUser(LoginView):
    """
    That class to login a user of the site
    who are in the data base user admin
    """
    template_name = 'accounts/login.html'
    success_url = '/'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = ''
        return context

    
   

class LogoutView(LogoutView):
    """ That class to login out a user of site"""

    def post(self, request):
        print('je vais me logout')
        logout(request)
        # Redirect to a accueil page.
        return HttpResponseRedirect('/')

class RegistrationView(View):
    form_class = CreatUserForm
    initial = {'key': 'value'}
    template_name = 'accounts/register.html'

    def get(self,request, *args, **kwargs):
        form = self.form_class(initial=self.initial)

        context = {'form': form, 'next': request.GET.get ('next', '')}
        return render(request, self.template_name, context)

    def post(self, request, *args,**kwargs):
        form = self.form_class(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login((request, user))
                return HttpResponseRedirect("/")
            else:
                context = {'form': form, 'next': request.GET.get('next', '')}
                return render(request,  self.template_name, context)
        else:
            form = self.form_class()
            context = {'form': form, 'next': request.GET.get('next', '')}
            return render(request, self.template_name, context)

    

