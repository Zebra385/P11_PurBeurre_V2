from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User, AnonymousUser
from store.models import Categories, Products, Attributs
from .views import AlimentListView
from .views import SauvegardeView
from django.urls import reverse
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

        request = RequestFactory().get('/', data={'auth_user_id': self.user})
        request.user = self.user
        print('self.user est ', self.user)

        view = AlimentListView()
        view.setup(request)
        # we fix the object _list because we do not call
        # SearchProduct as a view
        view.object_list = view.get_queryset()
        context = view.get_context_data()
        self.assertIn('list_substituts', context)

    # test if a user is connect
    def test_user_exist(self):
        request = self.factory.post('/store/aliment')
        request.user = AnonymousUser()
        print('le request.user est : ', request.user)
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
        Products.objects.create(name_product='Ravioli',
                                categorie_id=id_category)
        self.product = Products.objects.get(name_product='Ravioli')

    # test if a user is connect
    def test_user_exist(self):
        request = self.factory.post('/store/details', data={'choice': 1, })
        request.user = AnonymousUser()
        print('le request.user est : ', request.user)
        self.product = Products.objects.get(name_product='Ravioli')
        response = SauvegardeView.as_view()(request)
        # code 302 because redirection to the login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, 'store:login')

    # test the dowload in data base Attributs when the user is connect
    def test_load_attribut(self):
        request = self.factory.post('/store/aliment', data={'choice': 1, })
        request.user = self.user
        Products.objects.get(name_product='Ravioli')
        print(' dans test load attribut le request.user est : ', request.user.id)
        response = SauvegardeView.as_view()(request)
        # code 302 because redirection to the store/aliment
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, 'substituts:aliment')
