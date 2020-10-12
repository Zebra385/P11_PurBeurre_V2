from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from store.models import Products, Categories
from accounts.forms import CreatUserForm


class TestProject(StaticLiveServerTestCase):
    """
    Test fonctionnal to test if the user cans make correctly
    a research of a product in the first page
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(10)
        categorie = Categories.objects.create(name_category="pate a tartiner")
        cls.product = Products.objects.create(
            name_product="nutella", categorie_id=int(categorie.id)
        )

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_find_product(self):
        # We open the site with is localhost server
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        product_input = self.selenium.find_element_by_name("name_product")
        product_input.send_keys('nutella')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()

class TestResetPassword(StaticLiveServerTestCase):
    """
    Test fonctionnal to test if the user cans change 
    his password
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(10)
        form = CreatUserForm({
                    'username': 'jacob',
                    'email': 'jacob@orange.fr',
                    'password1': 'Marmote§',
                    'password2': 'Marmote§',
        })
        comment = form.save()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_reset_password_selenium(self):
        # We open the site with is localhost server
        self.selenium.get('%s%s' % (self.live_server_url, '/accounts/reset_password/'))
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys('jacob@orange.fr')
        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()
    
