"""
@author: Angus Whitehead
"""

import shelve


class FileHandler:

    def save(self, pokemon):
        database = shelve.open('pokedexData.db')
        database[pokemon.name] = pokemon

    def load_database(self):
        database = shelve.open('pokedexData.db')
        loaded_pokemon = []
        for i in database:
            loaded_pokemon = self.load_objects(i)
        return loaded_pokemon

    def load_objects(self, database):
        data = []
        for i in database:
            data = database[i]
        return data
