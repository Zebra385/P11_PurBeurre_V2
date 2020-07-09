from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class CreateUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	password = forms.CharField(max_length=32)

	class Meta:
		
		model = User
		fields = '__all__'


	def save(self, commit=True):
		user = super(CreateUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.password = self.cleaned_data['password']
		if commit:
			user.save()
		return user

class ProductForm(forms.Form):
    name_product = forms.CharField(label='Nom du produit recherché', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}),)

