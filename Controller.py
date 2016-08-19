"""

"""
from webScraperAssignment import web_scraper
from webScraperAssignment import Pokemon


class Controller:

    def get(self, url="http://pokemondb.net/pokedex/", gen=1, p_type="Fire"):
        my_web = web_scraper.WebScraper(url, gen, type)
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