
from webScraperAssignment import WebScraper
from webScraperAssignment import Pokemon
from datetime import datetime
from webScraperAssignment import Console
from webScraperAssignment import FileHandler


class Controller:
    pokedex = {}

    def __init__(self):
        self.my_console = Console.Console("(-o-)", """""", self)
        self.my_file_handler = FileHandler.FileHandler()

    def go(self):
        self.my_console.cmdloop()

    def get_from_web(self, url, gen, p_type):
        my_web = WebScraper.WebScraper(url, gen, p_type)
        list = my_web.list_gen()
        for species in list:
            pokemon = my_web.info_grab(species)
            self.create_pokemon(species, pokemon)
            print(species + " added")

    def save_data(self, name):
        pokemon = self.pokedex[name]
        self.my_file_handler.save(pokemon)

    def get_from_save(self):
        list = self.my_file_handler.load_database()
        for species in list:
            self.create_pokemon(species['name'], species)

    def create_pokemon(self, name, pokemon):
        self.pokedex[name] = Pokemon.Pokemon(pokemon["number"],
                                             pokemon["image"],
                                             name,
                                             pokemon["type"],
                                             pokemon["desc"],
                                             pokemon["height"],
                                             pokemon["weight"],
                                             datetime.now().ctime())
