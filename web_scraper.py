import requests
from bs4 import BeautifulSoup
import re

url = "http://pokemondb.net/pokedex/"


def list_gen(url):
    r = requests.get(url + "national").text

    soup = BeautifulSoup(r, "html.parser")
    container = soup.find('div', attrs={'class': 'infocard-tall-list'})
    cards = container.find_all('span')
    pokemon_info = []
    for card in cards:
        gen = card.find('a')
        type = card.find('small', attrs={'class': 'aside'}).text
        # print(type)
        # print(gen)
        if re.search('G1', gen['data-sprite']) and re.search('Fire', type):
            pokemon_info.append(card.find('a', attrs={'class': 'ent-name'}).text)
            # print(card.find('a', attrs={'class': 'ent-name'}))
        # pokemon_info = card.find_all('a', attrs={'class': 'ent-name'})
        # for pokemon in pokemon_info:
        #     pokemon_list.append(pokemon_info)
    return pokemon_info


def info_grab(pokemon):
    r = requests.get(url + pokemon).text
    soup = BeautifulSoup(r, "html.parser")
    desc = soup.find('div', attrs={'class': 'col desk-span-8 lap-span-6'})
    table = soup.find('div', attrs={'class': 'tabset-basics'})
    img = table.find('img')
    img = img['src']
    print(img)
    container = table.find('div', attrs={'class': 'col desk-span-4 lap-span-6'})
    basic_data = container.find('table', attrs={'class': 'vitals-table'})
    rows = basic_data.find_all('tr')
    for row in rows:
        if re.search('National', row.text):
            print(row.find('td').text)
        elif re.search('Type', row.text):
            print(row.find('td').text[1:])
        elif re.search('Height', row.text):
            print(row.find('td').text[row.find('td').text.index('(')+1:row.find('td').text.index(')')-1])
        elif re.search('Weight', row.text):
            print(row.find('td').text[row.find('td').text.index('(')+1:row.find('td').text.index(')')-3])

for pokemon in list_gen(url):
    print(pokemon)
    info_grab(pokemon)

