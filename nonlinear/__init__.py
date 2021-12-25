from scipy.misc import derivative
import numpy as np
from sympy import symbols, diff

class NonLinear:
    def __init__(self, funcs):
        self.funcs = funcs

    def fn(self, x):
        return self.funcs[0](x)

    def Fn(self, x):
        return np.array([self.funcs[i](x) for i in range(len(self.funcs))])

    def Jacobian(self, x):
        num = len(self.funcs)
        df = np.zeros((num,num),dtype=float)
        dx = 1e-8   
        x1 = np.copy(x)
        for i in range(0,num):
            for j in range(0,num):
                x1 = np.copy(x)
                x1[j] = x1[j] + dx   
                df[i,j] = (self.Fn(x1)[i] - self.Fn(x)[i])/dx
        df_rev = np.linalg.inv(df)
        return df_rev


    # 不动点迭代, x0 为初始点, delta 为要求的误差值
    def fixed_iter(self, x0, delta):
        x = x0
        next_x = x0
        count = 0
        while True:
            next_x = self.fn(x)
            err = abs(x - next_x)
            if err < delta:
                break
            else:
                x = next_x
            count += 1
        return (next_x, count)
    
    # 斯蒂芬森迭代法
    def stefenson_iter(self, x0, delta):
        x = x0
        y = x0
        z = x0
        next_x = x0
        count = 0
        while True:
            y = self.fn(x)
            z = self.fn(y)
            next_x = x - ((y - x)*(y - x) / (z - 2*y +x))
            err = abs(next_x - x)
            if err < delta:
                break
            else:
                x = next_x
            count += 1
        return (next_x, count)

    # 牛顿迭代法
    def newton_iter(self, x0, delta):
        x = x0
        next_x = x0
        count = 0
        while True:
            next_x = x - (self.fn(x)/derivative(self.fn, x))
            err = abs(next_x - x)
            if err < delta:
                break 
            else: 
                x = next_x
            count += 1
        return (next_x, count)

    # 多变量的不动点迭代
    def vec_fixed_iter(self, x0, delta):
        x = x0 
        next_x = x0
        count = 0
        while True:
            next_x = np.array([self.funcs[i](x) for i in range(len(self.funcs))])
            err = max(abs(x - next_x))
            if err < delta:
                break
            else:
                x = next_x
            count += 1
        return (next_x, count)

    # 非线性方程组的牛顿迭代法
    def vec_newton_iter(self, x0, delta):
        x = x0
        next_x = x0
        count = 0
        while True:
            next_x = x - np.dot(self.Jacobian(x), self.Fn(x))
            err = max(abs(next_x - x))
            if err < delta:
                break
            else:
                x = next_x
            count += 1
        return (x, count)
