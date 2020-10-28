from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User, AnonymousUser
from store.models import Categories, Products, Attributs
from .views import AlimentListView
from .views import SauvegardeView
from django.urls import reverse
from accounts.models import CustomUser

class AlimentTestCase(TestCase):
    """
    Test list of substitut in table Attributs
    """
    def setUp(self):
        """
        Every test needs access to the request factory
        """
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        self.name_product = 'Ravioli'
        product1 = Products.objects.create(
            name_product=self.name_product,
            nutriscore_product="d",
            categorie_id=id_category)
        product2 = Products.objects.create(
            name_product="Ravioli bio3",
            nutriscore_product="a",
            categorie_id=id_category)
        Attributs.objects.create(auth_user_id=self.user.id,
                                 attribut_choice=product1)
        Attributs.objects.create(auth_user_id=self.user.id,
                                 attribut_choice=product2)

    def test_environment_set_in_context(self):
        """
        test the context data
        """
        request = self.factory.get('/', data={'auth_user_id': self.user})
        request.user = self.user
        view = AlimentListView()
        view.setup(request)
        # we fix the object _list because we do not call
        # SearchProduct as a view
        view.object_list = view.get_queryset()
        context = view.get_context_data()
        self.assertIn('attributs_list', context)

    def test_user_exist(self):
        """
        test if a user is connect
        """
        request = self.factory.post('/store/aliment')
        request.user = AnonymousUser()
        response = AlimentListView.as_view()(request)
        # code 302 because redirection to the login page
        self.assertEqual(response.status_code, 302)


class SauvegardeTestCase(TestCase):
    """
    Detail save a substitut in datadabase Attributs
    """
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(username='jacob',
                                             email='jacob@orange.fr',
                                             password='top_secret')
        Categories.objects.create(name_category='pate')
        self.category = Categories.objects.get(name_category='pate')
        id_category = int(self.category.id)
        self.product = Products.objects.create(
            name_product='Ravioli',
            categorie_id=id_category)

    def test_anonymoususer_exist(self):
        """
        test if a user is connect
        """
        request = self.factory.post(
            '/store/aliment',
            data={'choice': self.product.pk, })
        request.user = AnonymousUser()
        response = SauvegardeView.as_view()(request)
        response.client = Client()
        # code 302 because redirection to the login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/store/aliment')

    def test_save_product(self):
        """
        test the dowload in data base Attributs when the user is connect
        """
        self.client.login(email='jacob@orange.fr', password='top_secret')
        response = self.client.post(
            reverse('substituts:sauvegarde'),
            data={'choice': self.product.pk, })
        # code 302 because redirection to the /substituts/aliment/
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/substituts/aliment/')
