import re
import numpy as np
from typing import List
from sys import path
path.append('..')
from point import Point

class LeastSquare:
    def __init__(self, a: float, b: float, c: int, samples: List[Point]):
        self.a = a 
        self.b = b
        self.c = c
        self.samples = samples
        self.n = len(samples)

    def fit(self):
        A = []
        B = []
        # print("n: {}".format(self.n))
        for i in range(0, self.n):
            row = []
            res = 0
            for j in range(0, self.n):
                for item in self.samples:
                    # print("x: {}, i: {}, j: {}".format(item.x, i, j))
                    res += pow(item.x, i + j)
                row.append(res)
            y = 0
            for item in self.samples:
                y += pow(item.x, i) * item.y
            A.append(row)
            B.append(y)
        # print("A: {}, B: {}".format(A, B))
        res = list(reversed(np.linalg.solve(A, B)))
        f = np.poly1d(res)
        self.f = f
    
    def cal(self, x):
        return self.f(x)