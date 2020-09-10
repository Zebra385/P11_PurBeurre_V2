from store import forms
from store.models import Products
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from store.forms import ProductForm
from django.views.generic import ListView
from django.views.generic.base import View
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.


from django.views.generic.detail import SingleObjectMixin
from store.models import Categories
"""
class CategoryProduct(SingleObjectMixin, ListView):
  
    We crete a special class to have a list that containts a special category
    we can use this class to show the substitut of a product
  
    paginate_by = 9
    template_name = 'store/categories_products.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Categories.objects.all())
        print('self.object vaut ', self.object)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('self.object vaut ', self.object)
        context['categories'] = self.object
        return context

    def get_queryset(self):
        return self.object.products_set.all()
"""
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
            self.text = None
            try:
                self.product = Products.objects.filter(name_product__iexact=self.name_product).first()
                try:
                    self.categori_produit = self.product.categorie
                    self.picture = self.product.picture
                    # To filter we looking for product than have the same category
                    # And we oder the list wiht the nutriscore of each product
                    category = self.categori_produit
                    self.essais = Products.objects.filter(categorie=category).order_by(
                        'nutriscore_product')[:24]

                    self.text = None
                    return self.essais
                except:
                    self.text = 'Produit absent de la base de données\
                            RETOURNER A L ACCUEIL'
                    self.picture= None       
                    self.essais = None
                    return self.essais
            except Products.DoesNotExist:
                # If the product do not exist in the data base we print a text
                # message:"your product does not exist in database,
                # return to accueil"
                self.name_product = None
                self.essais = None
                self.picture= None
                self.text = 'Produit absent de la base de données\
                            RETOURNER A L ACCUEIL'
                return self.text
      
        else:
            self.text = "Form non valid"
            self.name_product = None
            self.picture= None
            self.categori_produit = None
            self.essais = None
       

    def get_context_data(self, **kwargs):
        kwargs['name_product'] = self.name_product
        kwargs['essais'] = self.essais
        kwargs['text'] = self.text
        try: 
            kwargs['picture']=self.picture
        except Products.DoesNotExist:
            kwargs['picture']=None
                    
        return super(SearchProductView, self).get_context_data(**kwargs)

class DetailAlimentView(View):
    template_name = 'store/detail_aliment.html'
    model = Products

    def get_object(self, pk):
        
        return Products.objects.get(pk=pk)


    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        print('Dans affichage product', product)
        
       
        
        context = {'product': product}
       
        return render(request, self.template_name, context)

    """
    def post(self, request, product_id):
        print('product_id est:',product_id)
        # We select the product
        product=Products.objects.get( pk=product_id)
        
        print('Dans affichage product', product)
        
       
        
        context = {'product': product}
       
        return render(request, self.template_name, context)
    """