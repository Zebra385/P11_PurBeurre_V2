from django.test import TestCase
from django.urls import reverse
from accounts.forms import CreatUserForm


class MylogoutTestcase(TestCase):

    def test_logout(self):
        self.client.logout()
        response = self.client.post(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')


class RegistrationTestcase(TestCase):

    def test_form_valid(self):
        form = CreatUserForm({
                    'username': 'jacob',
                    'email': 'jacob@orange.fr',
                    'password1': 'Marmote§',
                    'password2': 'Marmote§',
        })
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.username, 'jacob')
        self.assertEqual(comment.email, 'jacob@orange.fr')

    def test_blank_data(self):
        form = CreatUserForm({
                    'username': '',
                    'email': '',
                    'password1': '',
                    'password2': '',
        })
        self . assertFalse(form . is_valid())


class MyloginTestcase(TestCase):

    def test_reset_password(self):
        self.client.login()
        response = self.client.post(reverse('accounts:reset_password'))
        self.assertEqual(response.status_code, 200)
