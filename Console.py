"""

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

    def do_scrape(self, line, url="http://pokemondb.net/pokedex/", gen=1, p_type="Fire"):
        """
        :param url: this is the base website that the program will go to in order to find the data it requires (leave
                    it blank to pass in the default)
        :param gen: this is the generation that you wish to search through (leave it blank to pass in the default)
        :param p_type: this is the type of pokemon to search
                       options are Normal, Fire, Fighting, Water ,Flying, Grass, Poison, Electric, Ground, Psychic, Rock, Ice,
                       Bug, Dragon, Ghost. (leave it blank to pass in the default)
        :return:
        """
        self.my_controller.get_from_web(url, gen, p_type)

    def do_read_file(self):
        pass

    def do_sort_weight(self, line):
        pass

    def do_sort_height(self, line):
        pass

    def do_get_desc(self, name):
        self.my_controller.data(name)


    def default(self, line):
        """Called on an input line when the command prefix is not recognized.

        If this method is not overridden, it prints an error message and
        returns.

        """
        self.stdout.write('(╯°□°）╯︵ ┻━┻ Unknown syntax: %s\n'%line)

