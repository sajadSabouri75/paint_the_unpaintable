import numpy as np


class Canvas:
    def __init__(self, **kwargs):
        self._size = kwargs['size']
        self._surface = np.zeros((self._size[0], self._size[1]))
