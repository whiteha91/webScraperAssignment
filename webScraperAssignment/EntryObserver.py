"""
@author: Angus Whitehead
"""
import Observer


class EntryObserver(Observer.Observer):

    def __init__(self, subject):
        self.subject = subject
        self.subject.subscribe(self)

    def update(self):
        species = self.subject.get_entry()
        if species != "":
            print(species, " added")
