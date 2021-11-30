class Legendre:
    def __init__(self, n: int):
        self.n = n 

    def fn(self, x):
        # 递归定义的勒让德多项式
        if self.n == 0:
            return 1
        elif self.n == 1:
            return x
        else:
            return (((2 * self.n) - 1) * x * self.fn(self.n - 1, x) - (self.n - 1) * self.fn(self.n - 2, x)) / float(self.n)
