from numpy import np
from typing import List
from . import Point

class PieceLinear:
    def __init__(self, samples: List[Point]):
        self.samples = samples

    def interp(self):
        pass