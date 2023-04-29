# igra pogađanja zastava zemalja svijeta

from distutils import core
import requests
from bs4 import BeautifulSoup
import os
import random
from PIL import Image

os.chdir('Fotografije')

flags_dir = 'flags/'

def download_image(src, name):
    print('Request: ', src)
    r = requests.get(src)
    data = r.content
    filepath = name + '.jpg'
    filepath = flags_dir + filepath
    with open(filepath, 'wb') as f:    # write binary mode
        f.write(data)

def build_flag_base():
    url = 'https://www.worldometers.info/geography/flags-of-the-world/'
    base_url = 'https://www.worldometers.info'

    if not os.path.exists(flags_dir):
        os.mkdir(flags_dir)
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    country_containers = soup.find_all('div', class_='col-md-4')
    for cc in country_containers:
        name = cc.get_text()
        name = name.strip()
        name = name.replace('-', '_')
        name = name.replace(' ', '_')
        name = name.replace('.', '')
        try:
            # src = cc.find('img').get('src')    # thumbnail
            src = cc.find('a').get('href')
        except AttributeError:
            continue
        src = base_url + src
        download_image(src, name)

if not os.listdir(flags_dir):
    build_flag_base()

print('Welcome the FlagGuessr!')
flags = os.listdir(flags_dir)
flags = [flags_dir + i for i in flags]

while True:
    N = input('Unesite broj zastava koliko želite pogađati: ')
    N = int(N)
    flags_to_guess = random.sample(flags, k=N)
    correct_guesses = 0
    for flag in flags_to_guess:
        correct_name = flag.replace(flags_dir, '').replace('.jpg', '').lower()
        img = Image.open(flag)
        img.show()
        name = input('Koja je ovo zemlja? ')
        # name = 'Bosnia and Herzegovina   '
        name = name.lower()    
        name = name.strip()    
        name = name.replace('-', '_')     
        name = name.replace(' ', '_')     
        name = name.replace('.', '')      
        if name == correct_name:
            print('Točno!')
            correct_guesses += 1
        else:
            print('Netočno, zemlja je ', correct_name)
    accuracy = correct_guesses / N
    accuracy *= 100
    accuracy = round(accuracy)
    print('Vaša točnost je: {} %'.format(accuracy))

    end = input('Želite li igrati ponovno (DA/NE)? ')
    if end.lower() == 'ne':
        break

