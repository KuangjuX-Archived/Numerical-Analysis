import re
import numpy as np
from typing import List
from sys import path
path.append('..')
from point import Point

class LeastSquare:
    def __init__(self, a: float, b: float, c: int, k: int, samples: List[Point]):
        self.a = a 
        self.b = b
        self.c = c
        self.samples = samples
        self.n = len(samples)
        self.k = k

    def fit(self):
        A = []
        B = []
        for i in range(0, self.k + 1):
            row = []
            for j in range(0, self.k + 1):
                res = 0
                for item in self.samples:
                    res += pow(item.x, i + j)
                row.append(res)
            y = 0
            for item in self.samples:
                y += pow(item.x, i) * item.y
            A.append(row)
            B.append(y)
        res = list(reversed(np.linalg.solve(A, B)))
        f = np.poly1d(res)
        self.f = f
    
    def cal(self, x):
        return self.f(x)