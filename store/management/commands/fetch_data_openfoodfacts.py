from django.core.management.base import BaseCommand

from store.models import Categories, Products
import requests


def package_json(url):
    """
    Function to return data in format json
    with a request from an url
    """
    r = requests.get(url)
    return r.json()


def package_product(name_category):
    """ function to load in data base the products"""

    # k is the number of the page on the site openfoodfacts
    for k in range(1, 20):
        # we load the different products in the same category
        package_json_product = package_json(
            f'https://fr.openfoodfacts.org/category/{name_category}/{k}.json')
        # we need categorie_id like a foreign key for
        # data base Products
        categorie_id = int(Categories.objects.get(
            name_category=name_category).id)

        # We take max 40 products per page
        for j in range(1, 40):
            try:
                name_product = package_json_product
                ['products'][j]['product_name']
                try:
                    Products.objects.update_or_create(
                        name_product=name_product,
                        nutriscore_product=package_json_product
                        ['products'][j]['nutriscore_grade'],
                        store_product=package_json_product
                        ['products'][j]['stores'],
                        picture=package_json_product
                        ['products'][j]['image_url'],
                        url_site=package_json_product
                        ['products'][j]['url'],
                        categorie_id=categorie_id,)
                except Products.DoesNotExist:
                    pass
                except ValueError:
                    pass
            except ValueError:
                pass


class Command(BaseCommand):

    help = 'Va permettre de remplir les tables(Categories et Products)\
            de notre base de données'

    def handle(self, *args, **options):
        # we load the different categories
        packages_json_categories = package_json(
            'https://fr.openfoodfacts.org/categories.json')
        # we take in table  store_Catégories the categories
        for i in range(1, 4):
            name_category = packages_json_categories['tags'][i]['name']
            # We fill the data base store.Categories
            Categories.objects.update_or_create(name_category=name_category)
            package_product(name_category)
        # we add in tables the category "Pâtes à tartiner aux noisettes"
        # to be sur that the product "nutella" exist in own data base
        for i in range(1, 4):
            name_category = "Pâtes à tartiner aux noisettes"
            # We fill the data base store.Categories
            Categories.objects.update_or_create(name_category=name_category)
            package_product(name_category)
