"""
@author: Angus Whitehead
"""


class Subject:

    def subscribe(self, observer):
        raise NotImplementedError

    def notify_all_observers(self, observer):
        raise NotImplementedError

    def get_entry(self, observer):
        raise NotImplementedError

    def get_selected(self, observer):
        raise NotImplementedError

    def get_stat(self, observer):
        raise NotImplementedError


