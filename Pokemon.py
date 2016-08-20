"""
    Created by Angus Whitehead
"""


class Pokemon:
    """
        This class is holding the information about each species
    """

    def __init__(self, index, image, name, type, desc, height, weight):
        self._index = index
        self._image = image
        self._name = name
        self._type = type
        self._desc = desc
        self._height = height
        self._weight = weight

    def get_type(self):
        return self._index

    def get_image(self):
        return self._image

    def get_index(self):
        return self._type

    def get_desc(self):
        return self._desc

    def get_height(self):
        return self._height

    def get_weight(self):
        return self._weight
