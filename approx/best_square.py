import numpy as np 
from . import inner_product_2, inner_product_3

class BestSquare:
    def __init__(self, k: int, a: float, b: float, c: int):
        self.k = k
        self.left = []
        self.right = []
        self.a = a
        self.b = b
        self.c = c

    def _make_matrix(self):
        # 建立矩阵
        for i in range(0, self.k + 1):
            row = []
            for j in range(0, self.k + 1):
                (res, _) = inner_product_3(i, j, self.a, self.b)
                row.append(res)
            (res, _) = inner_product_2(i, self.a, self.b, self.c)
            self.right.append(res)
            self.left.append(row)



    def fit(self):
        # 函数拟合，实际上就是根据次数解矩阵，最后把系数求出来
        self._make_matrix()
        res = list(reversed(np.linalg.solve(self.left, self.right)))
        f = np.poly1d(res)
        self.f = f

    def cal(self, x: int):
        res = self.f(x)
        return res