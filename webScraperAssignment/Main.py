"""
@author: Angus Whitehead
"""

import Controller
import EntryObserver
import StatsObserver


def start():
    c = Controller.Controller()
    EntryObserver.EntryObserver(c)
    StatsObserver.StatsObserver(c)
    c.go()

if __name__ == '__main__':
    start()
