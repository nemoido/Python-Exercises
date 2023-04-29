# povuci vremensku prognozu za korisnika sa stranice vrijeme.net

import requests
from bs4 import BeautifulSoup
import time

diac = {
    'č': 'c',
    'ć': 'c',
    'ž': 'z',
    'đ': 'd',
    'š': 's'
}

def process_city_name(name):
    name = name.lower()
    for key in diac:
        if key in name:
            value = diac[key]
            name = name.replace(key, value)
    name = name.replace(' na ', ' ')
    name = name.replace(' i ', ' ')
    name = name.replace(' ', '-')
    return name

url_template = 'https://www.vrijeme.net/hrvatska/'

def process(grad):
    grad = process_city_name(grad)
    url = url_template + grad

    r = requests.get(url)
    time.sleep(1)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    try:
        container = soup.find('div', class_='location-info block-01')
        if not container:
            return None, None
        description = container.find('p', class_='desc alt-01').text
        temperature = container.find('li', class_='temp').find('span', class_='val').text
    except AttributeError:
        return None, None
    return description, temperature

print('Dobrodošli u program Vrijeme!')
while True:
    mjesto = input('Unesite ime mjesta: ').strip()
    desc, temp = process(mjesto)
    if desc:
        print(f'U mjestu {mjesto} trenutno vrijeme je {desc} i temperatura je {temp}.')
    else:
        print('Nešto je pošlo po krivu!')
    kraj = input('Želite li još informacija (DA/NE)? ').strip().upper()
    if kraj == 'NE':
        print('Hvala na korištenju programa!')
        break