"""
@author: Angus Whitehead
"""
from webScraperAssignment import Sorter
from webScraperAssignment import Controller


def start():
    c = Controller.Controller(Sorter.Sorter())
    c.go()

if __name__ == '__main__':
    start()
