from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from store.models import Products, Categories
from accounts.forms import CreatUserForm
from accounts.models import CustomUser
from django.core import mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, get_user_model


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
        # we selection the field name_product
        product_input = self.selenium.find_element_by_name("name_product")
        # we enter the product than we research, here nutella
        product_input.send_keys('nutella')
        # We verify that this product exist
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()


class TestResetPassword(StaticLiveServerTestCase):
    """
    Test fonctionnal to test if the user cans change
    his password
    """
    @classmethod
    def setUpClass(cls):
        # it is to declare what we need in this test
        super().setUpClass()
        cls.selenium = webdriver.Firefox()
        cls.selenium.implicitly_wait(10)
        cls.user = CustomUser(
                    username='jacob',
                    email='jacob@orange.fr',
                    password='Marmote§',
        )
        cls.user.save()

    @classmethod
    def tearDownClass(cls):
        # to find the test , we quit the webdriver
        cls.selenium.quit()
        super().tearDownClass()

    def test_send_email(self):
        # Send message.
        mail.send_mail(
            'Réinitialisation du mot de passe',
            'Pour reinitialiser le message taper sur le lien: https://lien',
            'jacob@orange.fr', ['to@example.com'],
            fail_silently=False,
        )

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(
            mail.outbox[0].subject,
            'Réinitialisation du mot de passe')

    def test_reset_password_selenium(self):

        # We open the page in localhost server to reset our password
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/accounts/reset_password/')
            )
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys('jacob@orange.fr')
        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()

        # when we have receve a message, we click on a link
        # to can enter a new spassword
        # we need variables uid  and token whose send by the link
        uid = urlsafe_base64_encode(force_bytes(self.user.pk))
        token = default_token_generator.make_token(self.user)
        # We  ge to the page
        # {self.live_server_url}/accounts/reset/{uid}/{token}/
        # f behind is to convert the variable on  a string
        self.selenium.get(
            f"{self.live_server_url}/accounts/reset/{uid}/{token}/"
            )
        password1_input = self.selenium.find_element_by_name("new_password1")
        password2_input = self.selenium.find_element_by_name("new_password2")
        # we enter the new password
        password1_input.send_keys('elephant!')
        password2_input.send_keys('elephant!')
        self.selenium.find_element_by_xpath('//input[@type="submit"]').click()

        # We  ge to the page login to verify if jacob can login
        # with is new password
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/accounts/login/')
            )
        username_input = self.selenium.find_element_by_name("username")
        password_input = self.selenium.find_element_by_name("password")
        username_input.send_keys('jacob@orange.fr')
        password_input.send_keys('elephant!')
        self.selenium.find_element_by_xpath('//button[@type="submit"]').click()
        # Verify the page moncompte if Jacob is connect
        self.selenium.get(
            '%s%s' % (self.live_server_url, '/store/moncompte/')
            )
