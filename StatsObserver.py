"""
@author: Angus Whitehead
"""
import Observer


class StatsObserver(Observer.Observer):

    def __init__(self, subject):
        self.subject = subject
        self.subject.subscribe(self)

    def update(self):
        species = self.subject.get_selected()
        stat = self.subject.get_stat()
        if species is not None:
            print("Nation Number: " + str(species.get_index()))
            print("Image Link: " + species.get_image())
            print("Type: " + species.get_type())
            print("Pokedex Entry: " + species.get_desc())
            print("Height: " + str(species.get_height()) + "m")
            print("Weight: " + str(species.get_weight()) + "kg")
        elif stat[0] != "":
            strat = eval(stat[2] + '()')
            strat.show_results(stat)
