from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User, AnonymousUser
from store.models import Categories, Products, Attributs
from .views import AlimentListView
from .views import SauvegardeView
from django.urls import reverse
from django.contrib.auth import login 
from django.contrib.auth.models import Permission
# Create your tests here.


class AlimentTestCase(TestCase):
    def setUp(self):
            # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        self.name_product = 'Ravioli'
        product1 = Products.objects.create(name_product=self.name_product,
                                                nutriscore_product="d",
                                                categorie_id=id_category)
        product2 = Products.objects.create(name_product="Ravioli bio3",
                                                nutriscore_product="a",
                                                categorie_id=id_category)
        Attributs.objects.create(auth_user_id=self.user.id,
                                 attribut_choice=product1)
        Attributs.objects.create(auth_user_id=self.user.id,
                                 attribut_choice=product2)

    # test the context data
    def test_environment_set_in_context(self):

        request = self.factory.get('/', data={'auth_user_id': self.user})
        request.user = self.user
        # print('user est ', self.user)

        view = AlimentListView()
        view.setup(request)
        # we fix the object _list because we do not call
        # SearchProduct as a view
        view.object_list = view.get_queryset()
        context = view.get_context_data()
        self.assertIn('attributs_list', context)

    # test if a user is connect
    def test_user_exist(self):
        request = self.factory.post('/store/aliment')
        request.user = AnonymousUser()
        #print('le request.user est : ', request.user)
        response = AlimentListView.as_view()(request)
        # code 302 because redirection to the login page
        self.assertEqual(response.status_code, 302)


# Detail save a substitut in datadabase Attribut
class SauvegardeTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='jacob',
                                             email='jacob@…',
                                             password='top_secret')
        Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        self.product = Products.objects.create(name_product='Ravioli',
                                categorie_id=id_category)
        
        #produit = Products.objects.get(name_product='Ravioli')
  
    # test if a user is connect
    def test_anonymoususer_exist(self):
        
       
        request = self.factory.post('/store/aliment', data={'choice': self.product.id, })
        request.user = AnonymousUser()
        
        # product = Products.objects.get(name_product='Ravioli')
        response = SauvegardeView.as_view()(request)
        
        response.client = Client()
        
        # code 302 because redirection to the login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/store/aliment')
        

    # test the dowload in data base Attributs when the user is connect
    def test_user_exist(self):
        request = self.factory.post('/store/aliment', data={'choice': self.product.id,})
        request.user = self.user
        #print('le request.user  du test loadest : ', request.user)
        #client.login(username='jacob', password='top_secret')
        #print(' dans test load attribut le request.user est : ', request.user.id)
        self.client.login(username='jacob', password='top_secret')
        
        response = SauvegardeView.as_view()(request)
        response.client = Client()
        print('SauvegardeView.as_view()(request)', response)
        # request = RequestFactory().get('/', data={'name_product': "Ravioli"})
        # response =client.get('substituts:aliment')
        # code 302 because redirection to the store/resultats
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response.client, '/substituts/aliments/')

    # def test_load_attribut(self):
    #     # perm = Permission.objects.get(codename='can_approve_requests')
    #     # user.user_permissions.add(perm)
    #     print('Dans test load attributs self.user est:',self.user)
    #     #utilisateur = self.client.force_login(self.user, backend=None)
    #     utilisateur = self.client.login(username='jacob', password='top_secret')
    #     print('Dans test load attributs utilisateur est:', utilisateur)
    #     response = self.client.post('/store/aliment', data={'choice': self.product.id,})
    #     print('response est:', response)
    #     self.assertTemplateUsed(response, 'store/aliment.html')
       
       