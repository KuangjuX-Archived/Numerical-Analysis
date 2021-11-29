import numpy as np
from typing import List
from sys import path
path.append('..')
from point import Point, PolyFn

class PieceLinear:
    def __init__(self, samples: List[Point]):
        self.samples = samples
        self.poly = []

    def interp(self):
        n = len(self.samples)
        for i in range(0, n-1):
            # 一阶拉格朗日插值算表达式
            x1 = self.samples[i].x 
            x2 = self.samples[i + 1].x 
            f1 = self.samples[i].y 
            f2 = self.samples[i + 1].y 
            fn = (f1 / (x1 - x2)) * np.poly1d([1, -x2]) + (f2 / (x2 - x1)) * np.poly1d([1, -x1])
            self.poly.append(PolyFn(fn, x1, x2))

    def cal(self, x: float):
        for item in self.poly:
            if x >= item.a and x <= item.b:
                y = item.fn(x)
                return y 
        print("[Debug] 要计算的值不在给定区间中")
        return 0

    def vector_cal(self, x):
        y = []
        for item_x in x:
            item_y = self.cal(item_x)
            y.append(item_y)
        return y