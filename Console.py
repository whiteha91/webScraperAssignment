"""

"""
from cmd import Cmd
from webScraperAssignment import Controller

class Console (Cmd):
    """
    this is the user interface
    """
    prompt = "(-o-)"
    intro = ""

    def do_get_data(self, line, url, gen, type):
        controller = Controller()
        controller.get(url, gen, type)

    def do_sort_weight(self, line):
        pass

    def do_sort_height(self, line):
        pass

if __name__ == '__main__':
    Console().cmdloop()
