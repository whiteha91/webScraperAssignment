"""
@author: Angus Whitehead
"""

import Controller
import EntryObserver


def start():
    c = Controller.Controller()
    EntryObserver.EntryObserver(c)
    c.go()

if __name__ == '__main__':
    start()
