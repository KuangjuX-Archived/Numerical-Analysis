from scipy import integrate

class TargetFn:
    def __init__(self, c):
        self.c = c
        
    def fn(self, x: int):
        return (1 / ((self.c * x * x) + 1))

# def build_fn(x: int, c: int):
#     return (1 / ((c * x * x) + 1))

def product_fn(x, pow0, c):
    target = TargetFn(c)
    res = target.fn(x) * pow(x, pow0)
    return res

def product_fn_2(x, pow_1, pow_2):
    return (pow(x, pow_1) * pow(x, pow_2))
    

# 函数定积分
def integral(fn, a: int, b: int):
    return integrate.quad(fn, a, b)

# 求两函数内积
def inner_product(f1, f2, a: int, b: int):
    fn = f1 * f2 
    return integral(fn, a, b)

def inner_product_2(pow_0, a: int, b: int, c: int):
    return integrate.quad(product_fn, a, b, args=(pow_0, c))

def inner_product_3(pow_1, pow_2, a: int, b: int):
    f = product_fn_2
    return integrate.quad(f, a, b, args=(pow_1, pow_2))