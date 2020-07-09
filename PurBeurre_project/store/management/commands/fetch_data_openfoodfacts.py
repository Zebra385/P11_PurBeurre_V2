from django.core.management.base import BaseCommand

from store.models import Categories, Products
import requests

class Command(BaseCommand):
    
    help = 'Va permettre de remplir les tables de notre base de données'

    def handle(self, *args, **options):
        
        r1 = requests.get('https://fr.openfoodfacts.org/categories.json')
        packages_json_categories = r1.json()
        
        
        # we take in table  store_Catégories the categories
        for i in range(1, 200):
            # If key don't exist in the file json
                    #  to avoid mystake
           
            name_category = packages_json_categories['tags'][i]['name']
            
           
            Categories.objects.create(name_category=name_category)
            for k in range(1, 20):
                
                package_url = \
                    f'https://fr.openfoodfacts.org/category/{name_category}/{k}.json'
                try:
                    r2 = requests.get(package_url)
                
                    package_json_product = r2.json()
                    
                    categorie_id = int(Categories.objects.get(name_category=name_category).id)
                            
                    
                    for j in range(1, 40):
                        # If key don't exist in the file json
                        #  to avoid mystake
                        
                        try :
                            name_product = package_json_product['products'][j]['product_name']
                        
                            try:
                                nutriscore_product = package_json_product['products'][j]['nutriscore_grade']
                            except:
                                nutriscore_product ="?"
                            try:
                                store_product =  nutriscore_product = package_json_product['products'][j]['stores_tags']
                            except:
                                store_product = "Inconnu"
                            try:
                                site_url= package_json_product['products'][j]['url'] 
                            except:
                                site_url= "https://fr.openfoodfacts.org/"
                            try:
                                picture = package_json_product['products'][j]['image_url']
                            except :
                                picture= "?"          
                                               
                            Products.objects.create(
                                name_product=name_product,
                                nutriscore_product=nutriscore_product,
                                store_product=store_product,
                                picture= picture,
                                url_site=site_url,
                                categorie_id=categorie_id)
                            product_id=int(Products.objects.get(name_product=name_product).id)   
                            print('l id du produit est:',product_id)
                        except:
                            continue

                except:
                    continue   
                        
               
            