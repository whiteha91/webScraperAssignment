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
        if species:
            print(species[0])
            print("Nation Number: " + str(species[1].get_index()))
            print("Image Link: " + species[1].get_image())
            print("Type: " + species[1].get_type())
            print("Pokedex Entry: " + species[1].get_desc())
            print("Height: " + str(species[1].get_height()) + "m")
            print("Weight: " + str(species[1].get_weight()) + "kg")
