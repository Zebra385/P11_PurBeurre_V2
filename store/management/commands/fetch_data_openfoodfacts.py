from django.core.management.base import BaseCommand
from django.db import IntegrityError
from store.models import Categories, Products
import requests
import logging
logging.basicConfig( level=logging.DEBUG, filename='../env/var/log/debug_miseajour_db.log')

MY_CATEGORIES = [
    'Chocolats',
    'Pâtes à tartiner aux noisettes',
    'Boissons gazeuses',
    'Produits laitiers',
    'Petit-déjeuners',
    'Crèmes',
    'Soupes de légumes',
    'Fajitas',
    'Chips de pommes de terre',
    'Biscuits',
    'Jambons',
    'Fromages de vache',
    'Moutardes',
    'Poissons',
    'Plats préparés en conserve',
    'Poulets',
    'Matières grasses végétales',
    'Baguettes',
    'Yaourts nature',
    'Pâtes aux œufs',
    'Croissants',
    'Flocons de céréales',
    'Rillettes pur porc',
    'Thons blancs',
]


def package_json(url):
    """
    Function to return data in format json
    with a request from an url
    """
    r = requests.get(url)
    try:
        return r.json()
    except ValueError:
        print('pas de forme json')
        pass


def package_product(name_category):
    """
    Function to load in data base the products
    """
    categorie_id = int(Categories.objects.get(
        name_category=name_category).id)
    # we load the different products in the same category
    package_json_product = package_json(
        f'https://fr.openfoodfacts.org/category/{name_category}/2.json')
    print('...............................')
    # we need categorie_id like a foreign key for
    # data base Products
    # We take max 20 products per page
    for j in range(1, 20):
        try:
            name_product = package_json_product['products'][j]['product_name']
            print('le nouveau produit est :', j, name_product)
            try:
                Products.objects.get(name_product=name_product)
                pass
            except:
                Products.objects.update_or_create(
                    openfoodfats_id=package_json_product
                    ['products'][j]['id'],
                    categorie_id=categorie_id,
                    defaults={
                        'name_product': name_product,
                        'nutriscore_product': package_json_product
                        ['products'][j]['nutriscore_grade'],
                        'store_product': package_json_product
                        ['products'][j]['stores'],
                        'picture': package_json_product
                        ['products'][j]['image_url'],
                        'url_site': package_json_product
                        ['products'][j]['url'],
                        'fat': package_json_product
                        ['products'][j]['nutriments']['fat_100g'],
                        'saturated_fat': package_json_product
                        ['products'][j]['nutriments']['saturated-fat_100g'],
                        'sugars': package_json_product
                        ['products'][j]['nutriments']['sugars_100g'],
                        'salt': package_json_product
                        ['products'][j]['nutriments']['salt_100g'],
                    })
        except (ValueError, KeyError, IntegrityError, IndexError):
            pass


class Command(BaseCommand):

    help = 'Va permettre de remplir les tables(Categories et Products)\
            de notre base de données'

    def handle(self, *args, **options):
        """
        we load the different categories
        """
        for name_category in MY_CATEGORIES:
            # We fill the data base store.Categories
            Categories.objects.update_or_create(name_category=name_category)
            package_product(name_category)
