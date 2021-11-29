import numpy as np 
from . import inner_product

class BestSquare:
    def __init__(self, k: int, std_fn, a: int, b: int):
        self.k = k
        self.std_fn = std_fn
        self.left = []
        self.right = []
        self.a = a
        self.b = b

    def _make_matrix(self):
        # 建造矩阵
        for i in range(0, self.k + 1):
            row = []
            for j in range(0, self.k + 1):
                f1 = np.poly1d([1 for _ in range(0, i + 1)])
                f2 = np.poly1d([1 for _ in range(0, j + 1)])
                (res, _) = inner_product(f1, f2, self.a, self.b)
                # print("row res: {}".format(res))
                row.append(res)
            f1 = self.std_fn
            f2 = np.poly1d([1 for _ in range(0, i + 1)])
            (res, _) = inner_product(f1, f2, self.a, self.b)
            # print("col res: {}".format(res))
            self.right.append(res)
            self.left.append(row)
        print("left: {}, right: {}".format(self.left, self.right))



    def fit(self):
        # 函数拟合，实际上就是根据次数解矩阵，最后把系数求出来
        self._make_matrix()
        res = list(reversed(np.linalg.solve(self.left, self.right)))
        f = np.poly1d(res)
        print("f: {}".format(f))
        self.f = f

    def cal(self, x: int):
        res = self.f(x)
        return res