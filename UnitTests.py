import unittest
import WebScraper
import Controller


class UnitTests(unittest.TestCase):
    url = ""

    def setUp(self):
        self.url = "http://pokemondb.net/pokedex/"

    def test_list(self):
        p_list = ["Charmander",
                  "Charmeleon",
                  "Charizard",
                  "Vulpix",
                  "Ninetales",
                  "Growlithe",
                  "Arcanine",
                  "Ponyta",
                  "Rapidash",
                  "Magmar",
                  "Flareon",
                  "Moltres"]
        self.assertEqual(WebScraper.WebScraper(self.url, 1, "Fire").list_gen(),
                         p_list, "test failed")

    def test_image(self):
        img = 'https://img.pokemondb.net/artwork/flareon.jpg'
        controller = Controller.Controller()
        controller.get_from_web(self.url, 1, "Fire")
        self.assertEqual(controller.pokedex['Flareon'].get_image(), img,
                         "test failed")

    def test_pokemon_desc(self):
        expected = "\nCharmander is a Fire type Pokémon introduced in " \
                   "Generation 1. It is known as the Lizard Pokémon."
        controller = Controller.Controller()
        controller.get_from_web(self.url, 1, "Fire")
        self.assertEqual(controller.pokedex['Charmander'].get_desc(), expected,
                         "test failed")
    def test_

if __name__ == '__main__':
    unittest.main()
