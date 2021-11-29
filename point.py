import numpy as np
import random
import math 
from typing import List

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def derivative(self, d):
        self.d = d


class PolyFn:
    def __init__(self, fn: np.poly1d, a: float, b: float):
        # 多项式表达式
        self.fn = fn
        # 多项式区间，a 表示左边界, b 表示右边界
        self.a = a 
        self.b = b

# 对于给定三角函数求导并计算给定点导数
def point_derivative(x: float, c: float, d: float, e: float, f: float):
    y = c * d * math.cos(d * x) - e * f * math.sin(f * x)
    return y


# 根据给定区间以及点数对点进行采样
def random_sample(n: int, a: float, b: float, c: float, d: float, e: float, f: float):
    points = []
    for _ in range(n):
        x = a + random.random() * (b - a)
        y = c * math.sin(d * x) + e * math.cos(f * x)
        points.append(Point(x, y))
    return points

# 根据给定区间以及点数，计算固定步长进行采样
def fixed_sample(n: int, a: float, b: float, c: float, d: float, e: float, f: float):
    points = []
    step = (b - a) / n 
    for i in range(n):
        x = i * step + a 
        y = c * math.sin(d * x) + e * math.cos(f * x)
        points.append(Point(x, y))
    x = b 
    y = c * math.sin(d * x) + e * math.cos(f * x)
    points.append(Point(x, y))
    return points