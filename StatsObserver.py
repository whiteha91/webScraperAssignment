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
            if stat[2] == "min_weight":
                print("the lightest pokemon you have got data on is " + stat[0] +
                      " at only " + str(stat[1]) + "kg")
            elif stat[2] == "max_weight":
                print("the heaviest pokemon you have got data on is " + stat[0] +
                      " at a whooping " + str(stat[1]) + "kg")
            elif stat[2] == "avg_weight":
                print("the average weight of pokemon you have got data on is " +
                      str(stat[1]) + "kg")
            elif stat[2] == "min_height":
                print("the shortest pokemon you have got data on is " + stat[0] +
                      " at only " + str(stat[1]) + "m")
            elif stat[2] == "max_height":
                print("the tallest pokemon you have got data on is " + stat[0] +
                      " at a whooping " + str(stat[1]) + "m")
            elif stat[2] == "avg_height":
                print("the average height of pokemon you have got data on is " +
                      str(stat[1]) + "m")
