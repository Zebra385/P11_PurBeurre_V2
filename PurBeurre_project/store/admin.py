from django.contrib import admin

from .models import Products,Categories, Attributs

# Register your models here.



@admin.register(Categories)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Products)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Attributs)
class ContactAdmin(admin.ModelAdmin):
    pass