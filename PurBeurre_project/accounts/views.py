from django.shortcuts import render,redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout
# from .forms import CreateUserForm

from django.views.generic.base import View

# Create your views here.


# That will be use in th second version to can register evrybody
"""
def registration(request):
    form = CreateUserForm(request.POST)
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
        context = {'form': form}
        return render(request, 'registration/register.html', context)
"""

class LoginView(View):
    template_name = 'registration/login.html'
    

    

class LogoutView(View):

    def post(self,request):
        print('je vais me logout')
        logout(request)
        # Redirect to a success page.
        return HttpResponseRedirect('/')