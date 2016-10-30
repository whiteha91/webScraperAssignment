"""
@author: Angus Whitehead
"""
import WebScraper
import Pokemon
from datetime import datetime
import Console
import FileHandler
import StatisticCalculator


class Controller:
    pokedex = {}
    selected_pokemon = [2]
    last_entry = ""
    observers = []

    def __init__(self):
        self.my_console = Console.Console("(-o-)",
                                          """"Welcome to the personal pokemon encyclopedia (or pokedex for short)
        type help or '?' to see a list of commands""", self)
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

    def save_data(self, name):
        pokemon = self.pokedex[name]
        self.my_file_handler.save(pokemon)
        print("pokemon instance saved")

    def get_from_save(self):
        p_list = self.my_file_handler.load_database()
        for species in p_list:
            self.pokedex[species.name] = species
            self.last_entry = species.name
            self.notify_all_observers()
            self.last_entry = ""

    def create_pokemon(self, name, pokemon):
        self.pokedex[name] = Pokemon.Pokemon(
            pokemon, name, datetime.now().ctime())
        self.last_entry = name
        self.notify_all_observers()
        self.last_entry = ""

    def get_stats(self, name):
            self.selected_pokemon[0] = name
            self.selected_pokemon[1] = self.pokedex[name]
            self.notify_all_observers()
            self.selected_pokemon.clear()

    def get_min_weight(self):
        lightest = self.my_Calc.get_min(self.pokedex, "weight")
        weight = self.pokedex[lightest].get_weight()
        print("the lightest pokemon you have got data on is " + lightest +
              " at only " + str(weight) + "kg")

    def get_max_weight(self):
        heaviest = self.my_Calc.get_max(self.pokedex, "weight")
        weight = self.pokedex[heaviest].get_weight()
        print("the heaviest pokemon you have got data on is " + heaviest +
              " at a whooping " + str(weight) + "kg")

    def get_avg_weight(self):
        avg = self.my_Calc.get_avg(self.pokedex, "weight")
        print("the average weight of pokemon you have got data on is " +
              str(avg) + "kg")

    def get_min_height(self):
        shortest = self.my_Calc.get_min(self.pokedex, "height")
        height = self.pokedex[shortest].get_height()
        print("the shortest pokemon you have got data on is " + shortest +
              " at only " + str(height) + "m")

    def get_max_height(self):
        tallest = self.my_Calc.get_max(self.pokedex, "height")
        height = self.pokedex[tallest].get_height()
        print("the tallest pokemon you have got data on is " + tallest +
              " at a whooping " + str(height) + "m")

    def get_avg_height(self):
        avg = self.my_Calc.get_avg(self.pokedex, "height")
        print("the average height of pokemon you have got data on is " +
              str(avg) + "m")

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify_all_observers(self):
        for observer in self.observers:
            observer.update()

    def get_entry(self):
        return self.last_entry

    def get_selected(self):
        return self.selected_pokemon
