# program koji preuzima sve naslovne slike knjiga s books.toscrape.com - žanr horor

import os
import time

import requests
from bs4 import BeautifulSoup

# if not os.path.exists(output_dir):
#     os.mkdir(output_dir)

os.chdir('Scraping/Books')

# url = 'https://books.toscrape.com/media/cache/f7/b7/f7b73392b12909a1e8261ef3f96c5fd1.jpg'

# r = requests.get(url)
# data = r.content

# filepath = 'knjiga.jpg'
# with open(filepath, 'wb') as f:    # write binary mode
#     f.write(data)

def save_image(image_url):
    print('Request: ', image_url)
    r = requests.get(image_url)
    time.sleep(1)
    data = r.content
    filepath = image_url.split('/')[-1]
    filepath = filepath[-10:]
    with open(filepath, 'wb') as f:    # write binary mode
        f.write(data)

url = 'https://books.toscrape.com/catalogue/category/books/horror_31/index.html'
base_url = 'https://books.toscrape.com/'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data, 'html.parser')
image_containers = soup.find_all('div', class_='image_container')
for ic in image_containers:
    href = ic.find('a').get('href').replace('../', '')
    src = ic.find('img').get('src').replace('../', '')
    href = 'catalogue/' + href
    href = base_url + href
    src = base_url + src
    save_image(src)