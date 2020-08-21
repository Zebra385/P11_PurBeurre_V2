from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreatUserForm(UserCreationForm):
    email = forms.EmailField(label='Courriel')
    password = forms.CharField(label='Mot de passe', widget = forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ['first_name', 'email', 'password1','password2']
    
    """    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(UserCreationForm, self).__init__(*args, **kwargs)
    """
    def save(self, commit=True):
        user = super(CreatUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password']
        if commit:
            user.save()
        return user


