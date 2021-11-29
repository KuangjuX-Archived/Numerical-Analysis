from sys import path
path.append('..')
from point import Point
from typing import List
import numpy as np

def point_test(simu_fn, points: List[Point]):
    y1 = simu_fn(np.array([points[i].x for i in range(len(points))]))
    err = [abs(y1[i] - points[i].y) for i in range(len(points))]
    for i in range(len(points)):
        print("插值法计算的结果为：{}, 原函数计算的结果为: {}, 误差为: {}".format(y1[i], points[i].y, err[i]))








