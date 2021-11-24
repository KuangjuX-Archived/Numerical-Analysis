import numpy as np
from typing import List
from .import Point 


class Vandermonde:
    def __init__(self, samples: List[Point]):
        self.samples = samples

    def interp(self):
        # 生成矩阵
        samples = self.samples
        n = len(samples)
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