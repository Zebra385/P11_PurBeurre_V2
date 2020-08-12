from django.test import TestCase, RequestFactory
from django.test import Client
from django.urls  import reverse
from django.contrib.auth.models import User, AnonymousUser
from .models import Categories, Products, Attributs
from .views import AccueilView
from .views import ResultatsView
from .views import MoncompteView
from .views import CopyrightView
from .views import AlimentListView
from .views import SearchProductView
from .views import SauvegardeView
# Create your tests here.

#Test accueil page
class AccueilPageTestCase(TestCase):
     # test that accueil page returns a 200 if the item exists.
    def test_accueil_page(self):
        response = self.client.get(reverse('accueil'))

        self.assertEqual(response.status_code, 200)
"""
#Test copyright page
class CopyrightPtageTestCase(TestCase):
     # test that copyright page returns a 200 if the item exists.
    def test_copyright_page(self):
        response = self.client.get(reverse('copyright'))

        self.assertEqual(response.status_code, 200)
"""








# Detail SearchProduct
class SearchProducteTestCase(TestCase):

    def setUp(self):
        pate = Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        self.name_product='Ravioli'
        Products.objects.create(name_product=self.name_product, nutriscore_product="d",categorie_id=id_category)
        Products.objects.create(name_product="Ravioli bio3", nutriscore_product="a",categorie_id=id_category)
        self.product = Products.objects.get(name_product='Ravioli')
        
    # test the context data
    def test_environment_set_in_context(self):

        request = RequestFactory().get('/',data={'name_product':"Ravioli"})
        view = SearchProductView()
        view.setup(request)
        # we fix the object _list because we do not call SearchProduct as a view
        view.object_list = view.get_queryset()

        context = view.get_context_data()
        self.assertIn('essais', context)
        self.assertIn('name_product', context)
       
    # test that Resultat page returns a 200 if the product exists
    def test_search_product_page_return_200(self):
        name_product = self.product.name_product
        print('le produit est : ',name_product)
        response = self.client.get(reverse('store:search_product'),name_product=name_product)
        
        
        self.assertEqual(response.status_code, 200)
    

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

#Detail save a substitut in datadabase Attribut
class SauvegardeTestCase(TestCase):

    def setUp(self):
         # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        


        pate = Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        Products.objects.create(name_product='Ravioli', categorie_id=id_category)
        self.product = Products.objects.get(name_product='Ravioli')
       



        """
    # test if a user is connect
    def test_user_exist(self):
        request= self.factory.post('/store/details', data={'choice': 1,})
        request.user= AnonymousUser()
        print('le request.user est : ', request.user)
        self.product = Products.objects.get(name_product='Ravioli')
        attribut_choice = self.product.name_product
        response = SauvegardeView.as_view()(request)
        # code 302 because redirection to the login page
        self.assertEqual(response.status_code, 302)
"""
    #test the dowload in data base Attributs when the user is connect
    def test_load_attribut(self):
       
        request= self.factory.post('/store/aliment', data={'choice': 1,})
        request.user= self.user
        
        Products.objects.get(name_product='Ravioli')
        print(' dans test load attribut le request.user est : ', request.user.id)
        
        
        response = SauvegardeView.as_view()(request)
        # code 302 because redirection to the store/aliment
        self.assertEqual(response.status_code, 302)
      