from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from store.models import Products, Categories


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
