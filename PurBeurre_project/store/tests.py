from django.test import TestCase
from django.test import Client
from django.urls  import reverse
from django.contrib.auth.models import User
from .models import Categories, Products, Attributs
# Create your tests here.

#Test accueil page
class AccueilPageTestCase(TestCase):
     # test that accueil page returns a 200 if the item exists.
    def test_accueil_page(self):
        response = self.client.get(reverse('accueil'))

        self.assertEqual(response.status_code, 200)

# Detail SearchProduct
class SearchProducteTestCase(TestCase):

    def setUp(self):
        pate = Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        Ravioli = Products.objects.create(name_product='Ravioli', categorie_id=id_category)
        self.product = Products.objects.get(name_product='Ravioli')
        

    # test that Resultat page returns a 200 if the product exists
    def test_search_product_page_return_200(self):
        name_product = self.product.name_product
        print('le produit est : ',name_product)
        response = self.client.get(reverse('store:search_product'),name_product=name_product)
        
        
        self.assertEqual(response.status_code, 200)

   

#Detail save a substitut in datadabase Attribut
class SauvegardeTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='jean', password='mpjean3!', email='jean@orange.fr')
        self.client = Client() # May be you have missed this line

        pate = Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        Ravioli = Products.objects.create(name_product='Ravioli', categorie_id=id_category)
        self.product = Products.objects.get(name_product='Ravioli')




    # test if a user is connect
    def test_user_exist(self):
        name_person_id = None
        attribut_choice = self.product.name_product
        response = self.client.get(reverse('store:sauvegarde'), name_person_id=name_person_id, attribut_choice=attribut_choice)
        # code 302 because redirection to the login page
        self.assertEqual(response.status_code, 302)


    #test the dowload in data base Attributs when the user is connect
    def test_load_attribut(self):
        self.person=self.client.force_login(self.user)
        #self.person=self.client.login(username=self.user.username, password='mpjean3!')
        print('la person connecté est;', self.person)    
        attribut_choice = self.product.id
        choice=self.product.id
        print('l attribut est : ', attribut_choice)
        print('l id du user est : ', self.user.id)
        response = self.client.post(reverse('store:sauvegarde'),args=(choice,),name_person_id=self.user.id, attribut_choice=attribut_choice)
        #response = self.client.post(reverse('store:sauvegarde'), choice=choice)
        print('reponse avec user connecté est:', response)              
        self.assertEqual(response.status_code, 200)
      