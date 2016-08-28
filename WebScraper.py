"""
@author: Angus Whitehead
"""

import requests
from bs4 import BeautifulSoup
import re


class WebScraper:

    def __init__(self, the_url, gen, p_type):
        self.url = the_url
        self.gen = gen
        self.type = p_type

    def list_gen(self):
        r = requests.get(self.url + "national").text
        soup = BeautifulSoup(r, "html.parser")
        container = soup.find('div', attrs={'class': 'infocard-tall-list'})
        cards = container.find_all('span')
        pokemon_list = []
        for card in cards:
            gen = card.find('a')
            type_info = card.find('small', attrs={'class': 'aside'}).text
            # print(type_info + ' ' + self.type)
            # print(gen)
            if re.search('G' + str(self.gen), gen['data-sprite']) and \
                    re.search(self.type, type_info):
                pokemon_list.append(card.find('a', attrs={'class': 'ent-name'})
                                    .text)
                # print(card.find('a', attrs={'class': 'ent-name'}))
            # pokemon_list = card.find_all('a', attrs={'class': 'ent-name'})
            # for pokemon in pokemon_list:
            #     pokemon_list.append(pokemon_list)
        return pokemon_list

    def info_grab(self, pokemon,):
        r = requests.get(self.url + pokemon).text
        s = BeautifulSoup(r, "html.parser")
        desc = s.find('div',
                      attrs={'class': 'col desk-span-8 lap-span-6'}).text[:-1]
        table = s.find('div', attrs={'class': 'tabset-basics'})
        img = table.find('img')['src']
        container = table.find('div',
                               attrs={'class': 'col desk-span-4 lap-span-6'})
        basic_data = container.find('table', attrs={'class': 'vitals-table'})
        rows = basic_data.find_all('tr')
        number, pokemon_type, height, weight = 0, "", 0.0, 0.0
        for row in rows:
            if re.search('National', row.text):
                number = int(row.find('td').text)
            elif re.search('Type', row.text):
                pokemon_type = row.find('td').text[1:]
            elif re.search('Height', row.text):
                height = float(row.find('td').text[row.find('td').
                               text.index('(')+1:row.find('td').
                               text.index(')')-1])
            elif re.search('Weight', row.text):
                weight = float(row.find('td').text[row.find('td').text.
                               index('(')+1:row.find('td').text.index(')')-3])
        return {"name": pokemon,
                "image": img,
                "number": number,
                "type": pokemon_type,
                "desc": desc,
                "height": height,
                "weight": weight}
