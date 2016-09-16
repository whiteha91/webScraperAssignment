"""
@author: Angus Whitehead
"""


class StatisticCalculator:

    def get_min_weight(self, pokedex):
        min_weight = 1000000000
        lightest_pokemon = ""
        for name in pokedex:
            if pokedex[name].get_weight() < min_weight:
                min_weight = pokedex[name].get_weight()
                lightest_pokemon = name
        return lightest_pokemon

    def get_max_weight(self, pokedex):
        max_weight = -1
        heaviest_pokemon = ""
        for name in pokedex:
            if pokedex[name].get_weight() > max_weight:
                max_weight = pokedex[name].get_weight()
                heaviest_pokemon = name
        return heaviest_pokemon

    def get_avg_weight(self, pokedex):
        num_of_pokemon = len(pokedex)
        sum_of_weights = 0
        for name in pokedex:
            sum_of_weights += pokedex[name].get_weight()
        avg = sum_of_weights / num_of_pokemon
        return avg

    def get_min_height(self, pokedex):
        min_height = 1000000000
        shortest_pokemon = ""
        for name in pokedex:
            if pokedex[name].get_height() < min_height:
                min_height = pokedex[name].get_height()
                shortest_pokemon = name
        return shortest_pokemon

    def get_max_height(self, pokedex):
        max_height = -1
        tallest_pokemon = ""
        for name in pokedex:
            if pokedex[name].get_height() > max_height:
                max_height = pokedex[name].get_height()
                tallest_pokemon = name
        return tallest_pokemon

    def get_avg_height(self, pokedex):
        num_of_pokemon = len(pokedex)
        sum_of_heights = 0
        for name in pokedex:
            sum_of_heights += pokedex[name].get_height()
        avg = sum_of_heights / num_of_pokemon
        return avg
