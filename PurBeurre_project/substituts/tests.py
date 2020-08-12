from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls  import reverse
from django.contrib.auth.models import User, AnonymousUser
from .models import Categories, Products, Attributs
from .views import AccueilView
from .views import AlimentListView

# Create your tests here.


    

class AlimentTestCase(TestCase):

    def setUp(self):
          # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        pate = Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        self.name_product='Ravioli'
        self.product1 = Products.objects.create(name_product=self.name_product, nutriscore_product="d",categorie_id=id_category)
        self.product2 = Products.objects.create(name_product="Ravioli bio3", nutriscore_product="a",categorie_id=id_category)
        Attributs.objects.create(name_person=self.user, attribut_choice=self.product1)
        Attributs.objects.create(name_person=self.user, attribut_choice=self.product2)

    # test the context data
    def test_environment_set_in_context(self):

        request = RequestFactory().get('/',data={'name_person':self.user})
        request.user= self.user
        view = AlimentListView()
        view.setup(request)
        # we fix the object _list because we do not call SearchProduct as a view
        view.object_list = view.get_queryset()

        context = view.get_context_data()
        self.assertIn('list_substituts', context)
       

    # test if a user is connect
    def test_user_exist(self):
        request= self.factory.post('/store/aliment')
        request.user= AnonymousUser()
        print('le request.user est : ', request.user)
        
        response = AlimentListView.as_view()(request)
       
        # code 302 because redirection to the login page
        self.assertEqual(response.status_code, 302)