"""
@author: Angus Whitehead
"""
from webScraperAssignment import WebScraper
from webScraperAssignment import Pokemon
from datetime import datetime
from webScraperAssignment import Console
from webScraperAssignment import FileHandler
from webScraperAssignment import StatisticCalculator


class Controller:
    pokedex = {}

    def __init__(self):
        self.my_console = Console.Console("(-o-)", """""", self)
        self.my_file_handler = FileHandler.FileHandler()
        self.my_Calc = StatisticCalculator.StatisticCalculator()

    def go(self):
        self.my_console.cmdloop()

    def get_from_web(self, url, gen, p_type):
        my_web = WebScraper.WebScraper(url, gen, p_type)
        p_list = my_web.list_gen()
        for species in p_list:
            pokemon = my_web.info_grab(species)
            self.create_pokemon(species, pokemon)
            print(species + " added")

    def save_data(self, name):
        try:
            pokemon = self.pokedex[name]
            self.my_file_handler.save(pokemon)
            print("pokemon instance saved")
        except SystemError:
            print("pokemon instance could not be saved")

    def get_from_save(self):
        p_list = self.my_file_handler.load_database()
        for species in p_list:
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

    def get_stats(self, name):
            print(name)
            print("Nation Number: " + str(self.pokedex[name].get_index()))
            print("Image Link: " + self.pokedex[name].get_image())
            print("Type: " + self.pokedex[name].get_type())
            print("Pokedex Entry: " + self.pokedex[name].get_desc())
            print("Height: " + str(self.pokedex[name].get_height()) + "m")
            print("Weight: " + str(self.pokedex[name].get_weight()) + "kg")

    def get_min_weight(self):
        lightest = self.my_Calc.get_min_weight(self.pokedex)
        weight = self.pokedex[lightest].get_weight()
        print("the lightest pokemon you have got data on is " + lightest + " at only " + str(weight)+ "kg")

    def get_max_weight(self):
        heaviest = self.my_Calc.get_max_weight(self.pokedex)
        weight = self.pokedex[heaviest].get_weight()
        print("the heaviest pokemon you have got data on is " + heaviest + " at a wooping " +str(weight) + "kg")

    def get_avg_weight(self):
        avg = self.my_Calc.get_avg_weight(self.pokedex)
        print("the average weight of pokemon you have got data on is " + str(avg) + "kg")

    def get_min_height(self):
        shortest = self.my_Calc.get_min_height(self.pokedex)
        height = self.pokedex[shortest].get_height()
        print("the shortest pokemon you have got data on is " + shortest + " at only " + str(height) + "m")

    def get_max_height(self):
        tallest = self.my_Calc.get_max_height(self.pokedex)
        height = self.pokedex[tallest].get_height()
        print("the tallest pokemon you have got data on is " + "tallest" + " at a wooping " + str(height) + "m")

    def get_avg_height(self):
        avg = self.my_Calc.get_avg_height(self.pokedex)
        print("the average height of pokemon you have got data on is " + str(avg) + "m")
