from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreatUserForm(UserCreationForm):
	email = forms.EmailField(label='Courriel')
	password = forms.CharField(label='Mot de passe', widget = forms.PasswordInput)


	class Meta:
		model = User
		fields = '__all__'

	def save(self, commit=True):
		user = super(CreatUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.password = self.cleaned_data['password']
		if commit:
			user.save()
		return user

# Create your models here.

class ProductForm(forms.Form):
    """
    That form class to choice a product than we want looking for a substitut
    """
    name_product = forms.CharField(
        label='Nom du produit recherché',
        max_length=150,
        widget=forms.TextInput(attrs={'class': ' form-control'}),
        )
