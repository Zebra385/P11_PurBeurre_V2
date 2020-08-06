from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from store import forms
from store.models import Products, Attributs
from django.contrib.auth import authenticate, login, logout
# from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from store.forms import ProductForm

from django.contrib.auth.models import User
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
    

    


def logout_views(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')

class MoncompteView(TemplateView):
    template_name = 'store/moncompte.html'



class AccueilView(FormView):
    template_name = "store/accueil.html"
    form_class = ProductForm
    

class ResultatsView(TemplateView):
    template_name = "store/resultats.html"



#redirect when user is not logged in
@method_decorator(login_required(login_url='login'), name='dispatch')
class AlimentList(ListView):
    model = Attributs
    #user = User.objects.create(username='jean', password='mpjean3!', email='jean@orange.fr')
        
    
    #queryset = Attributs.objects.filter(name_person_id=user.id)
   
    template_name = 'store/aliment.html'
    

    def get_queryset(self):
        self.substituts = Attributs.objects.filter(name_person_id=self.request.user)
        return self.substituts
        #elif self.request.user.is_anonymous():
            

    def get_context_data(self):
        self.context={
        'list_substituts':[substitut.attribut_choice for substitut in self.substituts]
        }
        return self.context
  
    """   
def page_connection(request):
    template3 = loader.get_template('acccounts/login.html')
    return HttpResponse(template3.render(request=request))
"""


class SearchProductView(ListView):
    template_name='store/resultats.html'
    model = Products
    form_class = ProductForm
    context_object_name = "essais"

            
    def get_queryset(self):
        form = forms.ProductForm(self.request.GET)
        if form.is_valid():
            self.name_product = form.cleaned_data['name_product']
            print('form is valid name product est :', self.name_product)
        try:
            self.produit = Products.objects.get(name_product=self.name_product)
            print('form is valid name produit est :', self.produit)
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
        context = super(SearchProductView, self).get_context_data(**kwargs)
        context['name_product'] = self.name_product
        context['essais'] = self.essais
        context['text'] = self.text
        return context


@method_decorator(login_required(login_url='login'), name='dispatch')
class SauvegardeView(View):
    model = Attributs
    template_name = 'store/aliment.html'

    def post(self,request):
        # we take the id of the person who is connect
        name_person_id = int(request.user.id)
        print('Dans name_person_id:', name_person_id)
        # We select the choice
        selected_choice = request.POST.get('choice')
        print('Dans sauvegarde selection:', selected_choice)
        # we select the substitut
        attribut_choice = Products.objects.get(pk=selected_choice)
        print('Dans sauvegarde attribut_choice est : ', attribut_choice)
        # We load the datas in database
        load_choice = Attributs.objects.create(
            name_person_id=name_person_id,
            attribut_choice=attribut_choice,
            )
        # After we load the choice of substitut we return to page aliment
        print('Dans sauvegarde load_choice est : ', load_choice.id)
        return redirect('store:aliment')


class CopyrightView(TemplateView):
    template_name = 'store/copyright.html'


