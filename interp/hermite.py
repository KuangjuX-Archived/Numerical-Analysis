import numpy as np
from typing import List 
from . import Point, PolyFn

class Hermite:
    def __init__(self, samples: List[Point]):
        self.samples = samples
        self.poly = []

    def interp(self):
        pass