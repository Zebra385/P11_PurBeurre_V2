from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from store import forms
from store.models import Products, Attributs

# from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from store.forms import ProductForm

from django.contrib.auth.models import User
from django.views.generic.base import View
from django.views.generic import ListView

# Create your views here.




class MoncompteView(TemplateView):
    template_name = 'store/moncompte.html'



class AccueilView(FormView):
    template_name = "store/accueil.html"
    form_class = ProductForm
    




class CopyrightView(TemplateView):
    template_name = 'store/copyright.html'


class SearchProductView(ListView):
    template_name='store/resultats.html'
    model = Products
    form_class = ProductForm
    #context_object_name = "essais"

            
    def get_queryset(self):
        form = forms.ProductForm(self.request.GET)
        if form.is_valid():
            self.name_product = form.cleaned_data['name_product']
            #print('form is valid name product est :', self.name_product)
        else:
            self.name_product = None
        try:
            self.produit = Products.objects.get(name_product=self.name_product)
            #print('form is valid name produit est :', self.produit)
            self.categori_produit = self.produit.categorie
            self.essais = Products.objects.filter(
            categorie= self.categori_produit).order_by('nutriscore_product')
            self.text = None
            return self.essais 
        except Products.DoesNotExist:
            self.name_product = None
            self.essais =  None
            self.text = 'Produit absent de la base de données RETOURNER A L ACCUEIL' 
            return self.text

    
    def get_context_data(self, **kwargs):
        kwargs['name_product'] = self.name_product
        kwargs['essais'] = self.essais
        kwargs['text'] = self.text
        return super(SearchProductView, self).get_context_data(**kwargs)
