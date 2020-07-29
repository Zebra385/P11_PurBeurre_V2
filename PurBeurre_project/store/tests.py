from django.test import TestCase
from django.test import Client
from django.urls  import reverse
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
        product_name = self.product.name_product
        print('le produit est : ',product_name)
        response = self.client.get('store:search_product',name_product=product_name)
        self.assertEqual(response.status_code, 200)

    # test that Resultat page returns a 404 if the product does not exist
    def test_search_product_page_return_404(self):
        product_name= "banane"
        response = self.client.get('store:search_product', name_product=product_name)
        self.assertEqual(response.status_code, 404)

#Detail save a substitut in datadabase Attribut
class SauvegardeTestCase(TestCase):

    def setUp(self):
        
        pate = Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        Ravioli = Products.objects.create(name_product='Ravioli', categorie_id=id_category)
        self.product = Products.objects.get(name_product='Ravioli')




    # test if a user is connect
    def test_user_connect(self):
        c=Client()
        c.logout()
        name_person_id = None
        attribut_choice = self.product.name_product
        response = self.client.get('store:sauvegarde', attribut_choice=attribut_choice, name_person_id=name_person_id)
        self.assertEqual(response.status_code, 404)


    #test the dowload in data base Attributs
    def test_load_attribut(self):
        old_loading = Attributs.objects.count() # count Attributs before a request
        c = Client()
        person= c.login(username='marie', password='mp12345!')
        print('la personne est:', person)
        attribut_choice = self.product.name_product
        print('l attribut est : ', attribut_choice)
        
        response = self.client.get('store:sauvegarde', attribut_choice=attribut_choice, follow=True)
        new_loading = Attributs.objects.count() # cloadind after
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(new_loading, old_loading + 1) # make sure 1 loading was added
