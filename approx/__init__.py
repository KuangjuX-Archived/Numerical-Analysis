from scipy import integrate

# 函数定积分
def integral(fn, a: int, b: int):
    return integrate.quad(fn, a, b)

# 求两函数内积
def inner_product(f1, f2, a: int, b: int):
    fn = f1 * f2 
    return integral(fn, a, b)