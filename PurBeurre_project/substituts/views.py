from django.shortcuts import redirect
from django.http import HttpResponse

from store.models import Products, Attributs

# from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from store.forms import ProductForm

from django.contrib.auth.models import User
from django.views.generic.base import View

# Create your views here.

class ResultatsView(TemplateView):
    template_name = "store/resultats.html"



#redirect when user is not logged in
@method_decorator(login_required(login_url='login'), name='dispatch')
class AlimentListView(ListView):
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
        return redirect('substituts:aliment')