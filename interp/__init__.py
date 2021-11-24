import numpy as np
import random
import math 
from typing import List

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# 根据给定区间以及点数对点进行采样
def point_sample(n: int, a: float, b: float, c: float, d: float, e: float, f: float) -> List[Point]:
    points = []
    for _ in range(n):
        x = a + random.random() * (b - a)
        y = c * math.sin(d * x) + e * math.cos(f * x)
        points.append(Point(x, y))
    # x = np.linspace(1, 5, 30)
    # y = c * np.sin(d * x) + e * np.cos(f * x)
    # plt.plot(x, y)
    # plt.show()
    return points

def point_test(simu_fn, points: List[Point]):
    y1 = simu_fn(np.array([points[i].x for i in range(len(points))]))
    err = [abs(y1[i] - points[i].y) for i in range(len(points))]
    for i in range(len(points)):
        print("插值法计算的结果为：{}, 原函数计算的结果为: {}, 误差为: {}".format(y1[i], points[i].y, err[i]))



# 范德蒙矩阵解法，samples为采样点，n为采样数,返回对应的参数表达式
def vandermonde(samples: List[Point], n: int):
    # 生成矩阵
    matrix = []
    y = np.transpose(np.array([samples[i].y for i in range(n)]))
    for i, sample in enumerate(samples):
        if i == 0:
            matrix = np.array([[pow(sample.x, i) for i in range(n)]])
        else:
            matrix = np.append(matrix, [[pow(sample.x, i) for i in range(n)]], axis=0)
    # 计算范德蒙矩阵矩阵的结果   
    res = list(reversed(np.linalg.solve(matrix, y)))
    # 获取对应的多项式函数
    func = np.poly1d(res)
    # 画图进行模拟
    # x = np.linspace(1, 5, 30)
    # y = func(x)
    # plt.plot(x, y)
    # plt.show()
    # 返回多项式函数
    return func






