"""

"""
from webScraperAssignment import web_scraper
from webScraperAssignment import Pokemon


class Controller:

    def get(self, url, gen, p_type):
        my_web = web_scraper.WebScraper(url, gen, p_type)
        list = my_web.list_gen()
        for species in list:
            pokemon = my_web.info_grab(species)
            species = Pokemon.Pokemon(pokemon["number"],
                                      pokemon["image"],
                                      species,
                                      pokemon["type"],
                                      pokemon["desc"],
                                      pokemon["height"],
                                      pokemon["weight"])

    def data(self, pokemon):
        print(pokemon.get_desc())