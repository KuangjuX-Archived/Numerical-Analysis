import math
from numpy.core.fromnumeric import std
from scipy.integrate import quad

# 标准函数
def stdfn(x: float):
    return math.sqrt(x) * math.log(x)

def stdintegrate(a: float, b: float):
    res, _ = quad(stdfn, a, b)
    return res

# class Trapezodial:
#     def __init__(self, a: float, b: float, h: float):
#         self.a = a
#         self.b = b
#         self.h = h
#         self.samples = []

def trapezodial(a: float, b: float, h: float):
    res = stdfn(a) + stdfn(b)
    x = a + h 
    while x < b:
        res += 2 * stdfn(x)
        x += h 
    res *= (h / 2)
    return res
 
def romberg(a: float, b: float, delta: float):
    table = [[0 for _ in range(0, 100)] for _ in range(0, 100)]
    # for i in range(0, total):
    #     y = trapezodial(a, b, ((b - a) / (i + 1)))
    #     table[0][i] = y

    # std_integrate = stdintegrate(a, b)
    # for i in range(1, total):
    #     for j in range(i, total):
    #         y = (pow(4, i)/(pow(4, i) - 1)) * table[i-1][j-i+1] - (1/((pow(4, i) - 1))) * table[i-1][j-i]
    #         table[i][j] = y
    #         err = abs(std_integrate - y)
    #         if err < delta:
    #             print("标准函数积分值为: {}, 数值积分值为: {}, 误差为: {}".format(std_integrate, table[i][j], err))
    #             print("此时 m = {}, k = {}".format(i, j - i))
    #             return
    std_integrate = stdintegrate(a, b)
    table[0][0] = trapezodial(a, b, (b - a))
    k = 1
    err = abs(std_integrate - table[0][0])
    while err >= delta:
        for m in range(0, k + 1):
            if m == 0:
                table[k][m] = trapezodial(a, b, ((b - a) / pow(2, k)))
            else:
                table[k][m] = (pow(4, m)/(pow(4, m) - 1)) * table[k][m - 1] - (1/((pow(4, m) - 1))) * table[k-1][m - 1]
            err = abs(std_integrate - table[k][m])
            if err < delta:
                print("标准函数积分值为: {}, 数值积分值为: {}, 误差为: {}".format(std_integrate, table[k][m], err))
                print("此时 m = {}, k = {}".format(m, k))
                break
        k += 1
    
    

        
    
