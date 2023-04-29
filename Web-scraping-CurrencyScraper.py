# program za informacije o trenutnom tečaju spec. valute

import requests
from bs4 import BeautifulSoup

class Country:
    def __init__(self, ime, oznaka, kupovni, srednji, prodajni):
        self.ime = ime
        self.oznaka = oznaka
        self.kupovni = kupovni
        self.srednji = srednji
        self.prodajni = prodajni

    def display(self):
        print('-'*50)
        print('Zemlja: ', self.ime)
        print('Oznaka: ', self.oznaka)
        print('Kupovni: ', self.kupovni)
        print('Srednji: ', self.srednji)
        print('Prodajni: ', self.prodajni)
        print('-'*50)

url = 'https://www.hpb.hr/hr/tecajna-lista/2652'

r = requests.get(url)
data = r.text

soup = BeautifulSoup(data, 'html.parser')

table = soup.find('tbody', id='tecajbody')
table_rows = table.find_all('tr')

table_cells = []
for row in table_rows:
    cells = row.find_all('td')
    cells = [i.text for i in cells]
    table_cells.append(cells)
# table_cells = [[i.text for i in r.find_all('td')] for r in table_rows]

countries = []
for country in table_cells:
    name = country[0].rstrip()
    tag = country[1].split(' ')[0]
    kupovni = country[4]
    srednji = country[5]
    prodajni = country[6]
    c = Country(name, tag, kupovni, srednji, prodajni)
    countries.append(c)

# for country in countries:
#     country.display()

print('Dobrodošli u čitač valutnih tečaja!')
while True:
    kod = input('Unesite oznaku zemlje: ').strip().upper()
    for c in countries:
        if c.oznaka == kod:
            c.display()
            break
    else:
        print('Nemam informacija o toj valuti!')
    kraj = input('Želite li još informacija (DA/NE)? ').strip().upper()
    if kraj == 'NE':
        print('Hvala na korištenju programa!')
        break