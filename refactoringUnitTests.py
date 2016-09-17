import unittest
from WebScraper import WebScraper

class RefactoringUnitTests(unittest.TestCase):
    url = ""

    def setUp(self):
        self.url = "http://pokemondb.net/pokedex/"

    def test_initial_scrape(self):
        p_list = [
            "Charmander",
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
        self.assertEqual(WebScraper(self.url, 1, "Fire").list_gen(),
                         p_list, "Output has changed")

    def test_secondary_scrape(self):
        expected = {
            "name": "Charmander",
            "image": 'https://img.pokemondb.net/artwork/chaermander.jpg',
            "number": "004",
            "type": "Fire",
            "desc": "Charmander is a Fire type Pokémon introduced in\
             Generation 1. It is known as the Lizard Pokémon.",
            "height": "0.61",
            "weight": "8.5"
        }
        self.assertEqual(
            WebScraper.info_grab(self.url, 1, "Fire").info_grab("Charmander"),
            expected, "Output has changed")

if __name__ == '__main__':
    unittest.main()
