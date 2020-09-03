from accounts.forms import CreatUserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from accounts.forms import CreatUserForm
from django.contrib.auth.models import User
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
    
    template_name = 'accounts/register.html'

    def get(self,request, *args, **kwargs):
        
        form = self.form_class()

        context = {'form': form}
       
        return render(request, self.template_name, context)

    def post(self, request, *args,**kwargs):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            username = form.cleaned_data['username']
            print('username est:', username)
            password = form.cleaned_data['password1']
            email= form.cleaned_data['email']
            
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            
            
            return HttpResponseRedirect("/")
        else:
            print('form est:non valid')
            print(form.errors)
            context = {'form': form}
            return render(request,  self.template_name, context)
       

    

