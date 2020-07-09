from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from store import forms
from store.models import Persons
from store.models import Categories, Products
from django.contrib.auth import authenticate, login, logout, views
from django.contrib.auth.models import User
from .forms import CreateUserForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator

# Create your views here.
#create function to know is somebody is connect(logged_user_id=1)







from .forms import CreateUserForm


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
        context = {'form' : form}
        return render(request, 'registration/register.html', context) 

def logout_views(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')
        


def accueil(request):
    form2 = forms.ProductForm()
    template = loader.get_template('store/accueil.html')
    context = {
        'form':form2,
    }
    return HttpResponse(template.render(context, request))
        
   
          


def resultats(request):
    template1 = loader.get_template('store/resultats.html')
    return HttpResponse(template1.render(request=request))

def aliment(request):
    template2 = loader.get_template('store/aliment.html')
    return HttpResponse(template2.render(request=request))

def page_connection(request):
    template3 = loader.get_template('acccounts/login.html')
    return HttpResponse(template3.render(request=request))




def moncompte(request):
    template4 = loader.get_template('store/moncompte.html')
    return HttpResponse(template4.render(request=request))
            


def affichage_base(request):

    categories= Categories.objects.all()
    return render(request, 'store/affichage_base.html', {'categories': categories})

def affichage_base_product(request):

    products=Products.objects.all()
    return render(request, 'store/affichage_base_product.html', {'products': products})

def search_product(request):
    print(request.POST)
    # if this is a POST request we need to process the form data
    form2 = forms.ProductForm(data=request.POST)
    if form2.is_valid():

        name_product = form2.cleaned_data['name_product']
        print('le produit choisie est: ', name_product)
        produit = Products.objects.get(name_product=name_product)
        categori_produit = produit.categorie
        essais=Products.objects.filter(categorie=categori_produit).order_by('nutriscore_product')
        # print('essai:', essais[1])
        attributs= [produit.name_product for produit in Products.objects.filter(categorie=categori_produit)]
        list_attributs = " ".join(attributs)                   
        template = loader.get_template('store/resultats.html')
        context = {
        'name_product': name_product,
        'essais': essais,
        }
      
        return HttpResponse(template.render(context, request))
    else:
        name_product='jenesaispas'
        print('le produit choisie est: ', name_product)
                           
        template = loader.get_template('store/resultats.html')
        context = {
        'name_product': name_product,
        
        }
        return HttpResponse(template.render(context, request))

def detail(request):

    form2 = forms.ProductForm()
    name_product=form2.cleaned_data['name_product']
    print ('dans vu detail le prosduiist est:', name_product)
    produit = Products.objects.get(product_name=name_product)
    categori_produit = produit.categorie
    attributs= [produit.name_product for produit in Products.objects.filter(categorie=categori_produit)]
    # artists_name = " ".join(artists)

    context = {
        'list_attibuts': listattributs,
        'nutriscore': attributs.nutriscore,
        'thumbnail': attributs.picture,
    }
    return render(request, 'store/resultats.html', context)