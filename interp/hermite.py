import numpy as np
from typing import List 
from . import Point, PolyFn

class Hermite:
    def __init__(self, samples: List[Point]):
        self.samples = samples
        self.poly = []

    def interp(self):
        # 根据公式计算区间内的三次插值多项式
        n = len(self.samples)
        for i in range(0, n-1):
            x1 = self.samples[i].x
            x2 = self.samples[i+1].x
            y1 = self.samples[i].y
            y2 = self.samples[i+1].y
            d1 = self.samples[i].d 
            d2 = self.samples[i+1].d 

            item = y1 * (1 + 2 * np.poly1d([1, -x1]) / (x2 - x1)) * (np.poly1d([1, -x2]) / (x1 - x2)) * (np.poly1d([1, -x2]) / (x1 - x2))
            item += y2 * (1 + 2 * np.poly1d([1, -x2]) / (x1 - x2)) * (np.poly1d([1, -x1]) / (x2 - x1)) * (np.poly1d([1, -x1]) / (x2 - x1))
            item += d1 * (np.poly1d([1, -x1])) * (np.poly1d([1, -x2]) / (x1 - x2)) * (np.poly1d([1, -x2]) / (x1 - x2))
            item += d2 * (np.poly1d([1. -x2])) * (np.poly1d([1, -x1]) / (x2 - x1)) * (np.poly1d([1, -x1]) / (x2 - x1))
            self.poly.append(PolyFn(item, x1, x2))
    
    def cal(self, x: float):
            for item in self.poly:
                if x >= item.a and x <= item.b:
                    y = item.fn(x)
                    return y 
            print("[Debug] 要计算的值不在给定区间中")
            return 0


