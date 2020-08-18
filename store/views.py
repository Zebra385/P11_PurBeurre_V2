from store import forms
from store.models import Products
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from store.forms import ProductForm
from django.views.generic import ListView

# Create your views here.


class MoncompteView(TemplateView):
    """ That class to see who is connect or nobody"""
    template_name = 'store/moncompte.html'


class AccueilView(FormView):
    """ That class to get the acceuil page"""
    template_name = "store/accueil.html"
    form_class = ProductForm


class CopyrightView(TemplateView):
    """That class to give the url of all copyright use to build this site"""
    template_name = 'store/copyright.html'


class SearchProductView(ListView):
    """
    That class to search in the database if the product exist
    and list the possible substituts
    """
    template_name = 'store/resultats.html'
    model = Products
    form_class = ProductForm

    def get_queryset(self):
        form = forms.ProductForm(self.request.GET)
        if form.is_valid():
            self.name_product = form.cleaned_data['name_product']
        else:
            self.name_product = None
        try:
            self.product = Products.objects.get(name_product__iexact=self.name_product)
            self.categori_produit = self.product.categorie
            # To filter we looking for product than have the same category
            # And we oder the list wiht the nutriscore of each product
            category = self.categori_produit
            self.essais = Products.objects.filter(categorie=category).order_by(
                'nutriscore_product')
            self.text = None
            return self.essais
        except Products.DoesNotExist:
            # If the product do not exist in the data base we print a text
            # message:"your product does not exist in database,
            # return to accueil"
            self.name_product = None
            self.essais = None
            self.text = 'Produit absent de la base de données\
                         RETOURNER A L ACCUEIL'
            return self.text

    def get_context_data(self, **kwargs):
        kwargs['name_product'] = self.name_product
        kwargs['essais'] = self.essais
        kwargs['text'] = self.text
        return super(SearchProductView, self).get_context_data(**kwargs)