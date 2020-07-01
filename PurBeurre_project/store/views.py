from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from store import forms
from store.models import Persons
#from store.models import Categories, Products

# Create your views here.

def get_logged_user_from_request(request):
    if 'logged_user_id' in request.session:
        logged_user_id = request.session['logged_user_id']
        # We are looking for a person
        if len(Persons.objects.filter(id=logged_user_id)) == 1 :
            return Persons.objects.get(id=logged_user)
        else :
            return None
    else: 
        return None


def accueil(request):
    logged_user = get_logged_user_from_request(request)
    form = forms.LoginForm()
    if logged_user:

        template = loader.get_template('store/accueil.html')
        context = {
        'logged_user': logged_user,
        }
        return HttpResponse(template.render(context, request))
        
    else:
        template = loader.get_template('store/moncompte.html')
        context = {
        'form': form,
        }
        return HttpResponse(template.render(context, request))
          


def resultats(request):
    template1 = loader.get_template('store/resultats.html')
    return HttpResponse(template1.render(request=request))

def aliment(request):
    template2 = loader.get_template('store/aliment.html')
    return HttpResponse(template2.render(request=request))

def moncompte(request):
    # test if the form sends
    if len(request.POST) > 0:
        # test if the parameters was send
        form = forms.LoginForm()
        if form.is_valid():
            user_email = form.cleaned_data['email']
            logged_user = Persons.objects.get(email=user_email)
            request.session['logged_user_id'] = logged_user_id
            template = loader.get_template('store/accueil.html')
            return HttpResponse(template.render(request=request))
        else:
            template = loader.get_template('store/moncompte.html')
            context = {
            'form': form,
            }
            return HttpResponse(template.render(context, request))
            

    # the form was not send
    else:
        form = forms.LoginForm()
        template = loader.get_template('store/moncompte.html')
        context = {
        'form': form,
        }
        return HttpResponse(template.render(context, request))
"""
def affichage_base(request):

    categories= Categories.objects.all()
    return render(request, 'store/affichage_base.html', {'categories': categories})

def affichage_base_product(request):

    products=Products.objects.all()
    return render(request, 'store/affichage_base_product.html', {'products': products})
"""