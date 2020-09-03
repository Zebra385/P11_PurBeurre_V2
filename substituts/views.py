from django.shortcuts import redirect
from store.models import Products, Attributs
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.base import View

# Create your views here.


class ResultatsView(TemplateView):
    template_name = "store/resultats.html"


# redirect when user is not logged in
@method_decorator(login_required(login_url='login'), name='dispatch')
class AlimentListView(ListView):
    """
    class to show the substitut loading
    """
    model = Attributs
    template_name = 'store/aliment.html'
    
    context_object_name='attributs_list'
    paginate_by = 3

    def get_queryset(self):
       
        return Attributs.objects.filter(
            auth_user_id=self.request.user)
    """
    def get_context_data(self):
        list_substituts = [substitut.attribut_choice
                           for substitut in self.substituts]
        self.context = {'attributs_list': list_substituts}
        return self.context
    """

@method_decorator(login_required(login_url='login'),
                  name='dispatch')
class SauvegardeView(View):
    """
    class to load a substitut
    """
    model = Attributs
    template_name = 'store/aliment.html'

    def post(self, request):
        # we take the id of the person who is connect
        auth_user_id = int(request.user.id)
        print('Dans name_person_id:', auth_user_id)
        # We select the choice
        selected_choice = request.POST.get('choice')
        print('Dans sauvegarde selection:', selected_choice)
        # we select the substitut
        attribut_choice = Products.objects.get(pk=selected_choice)
        print('Dans sauvegarde attribut_choice est : ', attribut_choice)
        # We load the datas in database
        load_choice = Attributs.objects.create(
            auth_user_id=auth_user_id,
            attribut_choice=attribut_choice,
            )
        # After we load the choice of substitut we return to page aliment
        print('Dans sauvegarde load_choice est : ', load_choice.id)
        return redirect('substituts:aliment')
