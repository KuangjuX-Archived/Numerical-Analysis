import numpy as np
from typing import List
from sys import path
path.append('..')
from point import Point

class Largrange:
    def __init__(self, samples: List[Point]):
        self.samples = samples

    def interp(self):
        # 求拉格朗日每项的基函数
        n = len(self.samples)
        fn = np.poly1d([0])
        for i in range(0, n):
            item_fn = np.poly1d([1])
            div_num = 1
            for j in range(0, n):
                if i != j:
                    item_fn = item_fn * np.poly1d([1, -self.samples[j].x])
            for k in range(0, n):
                if i != k:
                    div_num = div_num * (self.samples[i].x - self.samples[k].x)
            item_fn = (item_fn / div_num) * self.samples[i].y
            fn = fn + item_fn
        self.fn = fn
        return fn

    def cal(self, x: float):
        return self.fn(x)
