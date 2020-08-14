from django.db import models
from django.conf import settings


class Categories(models.Model):
    """
    First class to load the categorie of the product on the site openfoodfacts
    """
    name_category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name_category

    class Meta:
        """
        That class to can choice a name of our database in  mode admin
        """
        verbose_name = "Categories"


class Products(models.Model):
    """
    Second class to load lot of product of each categories
    on the site openfoodfacts
    """
    name_product = models.CharField(max_length=150, unique=True)
    nutriscore_product = models.CharField(max_length=1)
    store_product = models.CharField(max_length=100)
    picture = models.URLField()
    url_site = models.URLField()
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_product

    class Meta:
        verbose_name = "Produits"


class Attributs(models.Model):
    """
    Fird class to save the attribut choice by the user
    """
    name_person = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    attribut_choice = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Attributs"
