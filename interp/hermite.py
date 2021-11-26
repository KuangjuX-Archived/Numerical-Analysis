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
            item = np.poly1d([0])
            x0 = self.samples[i].x 
            x1 = self.samples[i + 1].x 
            y0 = self.samples[i].y 
            y1 = self.samples[i + 1].y 
            d0 = self.samples[i].d 
            d1 = self.samples[i + 1].d 
            item += y0 * (1 + (2 / (x1 - x0)) * np.poly1d([1, -x0])) * (np.poly1d([1, -x1]) / (x0 - x1)) * (np.poly1d([1, -x1]) / (x0 - x1))
            item += y1 * (1 + (2 / (x0 - x1)) * np.poly1d([1, -x1])) * (np.poly1d([1, -x0]) / (x1 - x0)) * (np.poly1d([1, -x0]) / (x1 - x0))
            item += d0 * (np.poly1d([1, -x0])) * (np.poly1d([1, -x1]) / (x0 - x1)) * (np.poly1d([1, -x1]) / (x0 - x1))
            item += d1 * (np.poly1d([1, -x1])) * (np.poly1d([1, -x0]) / (x1 - x0)) * (np.poly1d([1, -x0]) / (x1 - x0))
            self.poly.append(PolyFn(item, x0, x1))
    
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


