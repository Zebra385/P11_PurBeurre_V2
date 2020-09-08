from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class CreatUserForm(UserCreationForm):
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
    
   
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Nom d\'utilisateur'
        self.fields['email'].label = 'Courriel'
    
   
    def save(self, commit=True):
        user = super(CreatUserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        # make_password to hashe the password
        user.password =  make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


