from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from store import forms
from store.models import Products, Attributs
from django.contrib.auth import authenticate, login, logout
# from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.


# That will be use in th second version to can register evrybody
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


def logout_views(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')


def accueil(request):
    form2 = forms.ProductForm()
    template = loader.get_template('store/accueil.html')
    context = {
        'form': form2,
    }
    return HttpResponse(template.render(context, request))


def resultats(request):
    template1 = loader.get_template('store/resultats.html')
    return HttpResponse(template1.render(request=request))


@login_required
def aliment(request):
    substituts = Attributs.objects.filter(name_person__id=request.user.id)
    template = loader.get_template('store/aliment.html')
    context = {
        'list_substituts':
        [substitut.attribut_choice for substitut in substituts],
    }
    return HttpResponse(template.render(context, request))


def page_connection(request):
    template3 = loader.get_template('acccounts/login.html')
    return HttpResponse(template3.render(request=request))


def moncompte(request):
    template4 = loader.get_template('store/moncompte.html')
    return HttpResponse(template4.render(request=request))


def search_product(request):
    print(request.GET)
    # if this is a POST request we need to process the form data
    form2 = forms.ProductForm(data=request.GET)
    if form2.is_valid():
        name_product = form2.cleaned_data['name_product']
        # produit = Products.objects.get(name_product=name_product)
        produit = get_object_or_404(Products, name_product=name_product)
        categori_produit = produit.categorie
        essais = Products.objects.filter(
            categorie=categori_produit).order_by('nutriscore_product')
        template = loader.get_template('store/resultats.html')
        context = {
            'name_product': name_product,
            'essais': essais,
        }
        return HttpResponse(template.render(context, request))
    else:
        name_product = 'Inconnu'
        template = loader.get_template('store/resultats.html')
        context = {
            'name_product': name_product,
                }
        return HttpResponse(template.render(context, request))


@login_required
def sauvegarde(request):
    # we take the id of the person who is connect
    name_person_id = int(request.user.id)
    # We select the choice
    selected_choice = request.POST.get('choice')
    print('selection:', selected_choice)
    # we select the substitut
    attribut_choice = Products.objects.get(pk=selected_choice)
    # We load the datas in database
    attribut_choice = Attributs.objects.create(
        name_person_id=name_person_id,
        attribut_choice=attribut_choice,
        )
    # After we load the choice of substitut we return to page aliment
    
    return redirect('store:aliment')

def copyright(request):
    template1 = loader.get_template('store/copyright.html')
    return HttpResponse(template1.render(request=request))