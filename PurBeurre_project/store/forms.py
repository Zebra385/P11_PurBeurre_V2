from django import forms
from store.models import Persons

class LoginForm(forms.Form):
	email = forms.EmailField(label='Courriel')
	password = forms.CharField(label='Mot de passe', widget = forms.PasswordInput)

	def clean(self):
		cleaned_data = super (LoginForm, self).clean()
		email = cleaned_data.get("email")
		password = cleaned_data.get("password")

		#Verify the two fields were valid
		if email and password:
			result = Persons.objects.filter(password=password, email=email)
			if len(result) !=1:
				raise forms.ValidationError("Adresse de courriel ou mot de passe éronné.")
		return cleaned_data
