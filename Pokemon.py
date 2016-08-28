"""
@author: Angus Whitehead
"""


class Pokemon:
    """
        This class is holding the information about each species
    """

    def __init__(self,
                 index,
                 image,
                 name,
                 p_type,
                 desc,
                 height,
                 weight,
                 date_added):
        self._index = index
        self._image = image
        self.name = name
        self._type = p_type
        self._desc = desc
        self._height = height
        self._weight = weight
        self._date_added = date_added

    def get_index(self):
        return self._index

    def get_image(self):
        return self._image

    def get_type(self):
        return self._type

    def get_desc(self):
        return self._desc

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight

    def get_date_added(self):
        return self._date_added
