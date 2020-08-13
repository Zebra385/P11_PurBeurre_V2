from django import forms


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
