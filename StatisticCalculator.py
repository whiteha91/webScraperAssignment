"""
@author: Angus Whitehead
"""


class StatisticCalculator:

    def get_min(self, pokedex, measurable):
        min_value = 1000000000
        pokemon = ""
        for name in pokedex:
            if measurable == "weight":
                value = pokedex[name].get_weight()
            else:
                value = pokedex[name].get_height()
            if value < min_value:
                min_value = value
                pokemon = name
        return pokemon

    def get_max(self, pokedex, measurable):
        max_value = -1
        pokemon = ""
        for name in pokedex:
            if measurable == "weight":
                value = pokedex[name].get_weight()
            else:
                value = pokedex[name].get_height()
            if value > max_value:
                max_value = value
                pokemon = name
        return pokemon

    def get_avg(self, pokedex, measurable):
        num_of_pokemon = len(pokedex)
        sum_of_values = 0
        for name in pokedex:
            if measurable == "weight":
                value = pokedex[name].get_weight()
            else:
                value = pokedex[name].get_height()
            sum_of_values += value
        avg = sum_of_values / num_of_pokemon
        return avg
