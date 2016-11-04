"""
@author: Angus Whitehead
"""
import WebScraper
import Pokemon
from datetime import datetime
import Console
import FileHandler
import StatisticCalculator
import Subject


class Controller(Subject.Subject):
    pokedex = {}
    selected_pokemon = None
    last_entry = ""
    observers = []
    stand_out = ["", 0, ""]

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
            self.selected_pokemon = self.pokedex[name]
            self.notify_all_observers()
            self.selected_pokemon = None

    def get_min(self, stat):
        lightest = self.my_Calc.get_min(self.pokedex, stat)
        weight = self.pokedex[lightest].get_weight()
        self.stand_out = [lightest, weight, "Min" + stat]
        self.notify_all_observers()
        self.stand_out = ["", 0, ""]

    def get_max(self, stat):
        heaviest = self.my_Calc.get_max(self.pokedex, stat)
        weight = self.pokedex[heaviest].get_weight()
        self.stand_out = [heaviest, weight, "Max" + stat]
        self.notify_all_observers()
        self.stand_out = ["", 0, ""]

    def get_avg(self, stat):
        avg = self.my_Calc.get_avg(self.pokedex, stat)
        self.stand_out = ["avg", avg, "Avg" + stat]
        self.notify_all_observers()
        self.stand_out = ["", 0, ""]

    def subscribe(self, observer):
        self.observers.append(observer)

    def notify_all_observers(self):
        for observer in self.observers:
            observer.update()

    def get_entry(self):
        return self.last_entry

    def get_selected(self):
        return self.selected_pokemon

    def get_stat(self):
        return self.stand_out
