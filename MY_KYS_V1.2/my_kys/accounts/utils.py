import json
import os
from django.conf import settings

def load_cities_from_json():
    # cities.json dosyasını okuma
    cities_file = os.path.join(settings.BASE_DIR,'data', 'cities.json')
    with open(cities_file, 'r', encoding='utf-8') as f:
        cities = json.load(f)
    return [(city['Id'], city['Name']) for city in cities]


def get_city_name(city_id):
    
    cities_file = os.path.join(settings.BASE_DIR, 'data','cities.json')
    with open(cities_file, 'r', encoding='utf-8') as f:
        cities = json.load(f)
        for city in cities:
            
            if int(city['Id']) == int(city_id):
               print(f'a {city_id}!')
               print(f'b {city['Id']}!') 
                
               return city['Name']
    return None