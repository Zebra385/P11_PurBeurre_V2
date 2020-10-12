from django.contrib import admin
from .models import Products, Categories, Attributs

# Register your models here.


@admin.register(Categories)
class CategorieAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Attributs)
class AttributAdmin(admin.ModelAdmin):
    pass
