import numpy as np
import math
from typing import List
from . import Point

class Netwon:
    def __init__(self, samples: List[Point]):
        self.table = []
        self.samples = samples

    # 计算均差
    def _div_diff(self, x1: float, x2: float, f1: float, f2: float):
        return (f2 - f1) / (x2 - x1)
    
    # 计算均差表
    def _div_table(self):
        n = len(self.samples)
        # 获得0阶均差，即所有采样点的函数值
        self.table.append([self.samples[i].y for i in range(n)])
        # 迭代 n - 1 次，获得所有均差值
        for i in range(1, n):
            # k 阶差商表
            k_table = [0 for _ in range(0, i)]
            for j in range(i, n):
                # 获得上一级的均差
                y1 = self.table[i - 1][j - 1]
                y2 = self.table[i - 1][j]
                # 获得对应的 x
                x1 = self.samples[j - i].x;
                x2 = self.samples[j].x;
                # 计算均差
                f = self._div_diff(x1, x2, y1, y2)
                k_table.append(f)
            self.table.append(k_table)
        print(self.table)
    
    # 牛顿插值法计算
    def netwon(self):
        # 获取均差表
        self._div_table()
        # 构造多项式参数