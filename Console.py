"""
@author: Angus Whitehead
"""

from cmd import Cmd


class Console (Cmd):
    """
    this is the user interface
    """
    prompt = ""
    intro = """"""
    my_controller = None

    def __init__(self, the_prompt, the_intro, the_controller):
        super(Console, self).__init__()
        self.prompt = the_prompt
        self.intro = the_intro
        self.my_controller = the_controller

    def do_scrape(self, line, url="http://pokemondb.net/pokedex/",
                  gen=1, p_type="Fire"):
        """
        :param url: this is the base website that the program will go to in
                order to find the data it requires (leave it blank to pass in
                 the default)
        :param gen: this is the generation that you wish to search through
                   (leave it blank to pass in the default of 1)
        :param p_type: this is the type of pokemon to search
                       options are Normal, Fire , Fighting, Water ,Flying,
                       Grass, Poison, Electric, Ground, Psychic,
                       Rock , Ice, Bug, Dragon, Ghost. (leave it blank to pass
                       in the default of fire)
        """
        self.my_controller.get_from_web(url, gen, p_type)

    def do_save(self, name):
        """
        this function saves the instance of the pokemon class
        :param name: this is the name of the pokemon whose instance you wish
                to save
        """
        name = name.title()
        try:
            self.my_controller.save_data(name)
        except SystemError:
            print("pokemon instance could not be saved")

    def do_load(self):
        """
        this function loads the saved instances of the pokemon class
        """
        try:
            self.my_controller.get_from_save()
        except IOError:
            print("pokemon not in database")

    def do_stats(self, name):
        """
        this function gathers the stored information on a pokemon species
        :param name: this is the name of the pokemon whose information you wish
         to view
        """
        name = name.title()
        try:
            self.my_controller.get_stats(name)
        except KeyError:
            print("Pokemon " + name + " doesn't exist in this generation")

    def do_max(self, stat):
        """
        this function displays the Pokemon with the largest stat requested
         eg min weight
        """
        self.my_controller.get_max(self, stat.title())

    def do_min(self, stat):
        """
        this function displays the pokemon with the smallest stat requested
        eg max weight
        """
        self.my_controller.get_min(self, stat.title())

    def do_average(self, stat):
        """
        this function displays the average stat requested of all pokemon stored
        eg average weight
        """
        self.my_controller.get_avg(self, stat.title())

    def do_exit(self, line):
        """
        this function allows the user to stop the command interpreter
        :return:
        """
        return True
