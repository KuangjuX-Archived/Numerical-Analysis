import numpy as np
from scipy.special import legendre
from scipy import integrate
from . import TargetFn, inner_product, inner_product_2, inner_product_3, inner_product_4, mul_fn

class BestSquare:
    def __init__(self, k: int, a: float, b: float, c: int):
        self.k = k
        self.left = []
        self.right = []
        self.a = a
        self.b = b
        self.c = c
        self.f = np.poly1d([0])

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

    def legrand_fit(self):
        # 使用勒让德多项式作为正交多项式进行拟合
        self.coefficients = []
        for i in range(0, self.k + 1):
            (res, _) = integrate.quad(mul_fn, -1, 1, args=(legendre(i), self.c))
            res *= ((2 * i + 1) / 2)
            # print("i: {}, res: {}".format(i, res))
            self.coefficients.append(res)
        # print("勒让德多项式系数: {}".format(self.coefficients))
        for i in range(0, self.k + 1):
            self.f += (self.coefficients[i] * legendre(self.k - i))

    def fit(self):
        # 函数拟合，实际上就是根据次数解矩阵，最后把系数求出来
        self._make_matrix()
        res = list(reversed(np.linalg.solve(self.left, self.right)))
        f = np.poly1d(res)
        self.f = f

    def cal(self, x: int):
        res = self.f(x)
        return res