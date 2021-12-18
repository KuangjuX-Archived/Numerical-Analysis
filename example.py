from approx import TargetFn
from approx.best_square import BestSquare
from approx.least_squares import LeastSquare
from integration import romberg, stdintegrate, trapezodial
from matrix import Matrix
import point
import interp
from draw import Drawer
from interp.hermite import Hermite
from interp.lagrange import Largrange
from interp.newton import Netwon
from interp.piece_linear import PieceLinear
from interp.vandermonde import Vandermonde

import numpy as np

def test_vandermonde():
    print("范德蒙德插值法")
    npoints = 10
    a = 0
    b = 5
    c = 1
    d = 1
    e = 1
    f = 1
    samples = point.random_sample(npoints, a, b, c, d, e, f)
    vandermonde = Vandermonde(samples)
    fn = vandermonde.interp()
    other_samples = point.random_sample(5, a, b, c, d, e, f)
    interp.point_test(fn, other_samples)
    drawer = Drawer()
    drawer.draw_interp(a, b, c, d, e, f, fn, 'Vandermonde Method')

def test_newton():
    print("牛顿插值法")
    npoints = 10
    a = 0
    b = 5
    c = 1
    d = 1
    e = 1
    f = 1
    samples = point.random_sample(npoints, a, b, c, d, e, f)
    newton = Netwon(samples)
    fn = newton.interp()
    other_samples = point.random_sample(5, a, b, c, d, e, f)
    interp.point_test(fn, other_samples)
    drawer = Drawer()
    drawer.draw_interp(a, b, c, d, e, f, fn, 'Newton Method')


def test_lagrange():
    print("拉格朗日插值法")
    npoints = 10
    a = 0
    b = 5
    c = 1
    d = 1
    e = 1
    f = 1
    samples = point.random_sample(npoints, a, b, c, d, e, f)
    lagrange = Largrange(samples)
    fn = lagrange.interp()
    other_samples = point.random_sample(5, a, b, c, d, e, f)
    interp.point_test(fn, other_samples)
    drawer = Drawer()
    drawer.draw_interp(a, b, c, d, e, f, fn, 'Lagrange Method')

def test_piecelinear():
    print("分段线性插值法")
    npoints = 1000
    a = 0
    b = 5
    c = 1
    d = 1
    e = 1
    f = 1
    samples = point.fixed_sample(npoints, a, b, c, d, e, f)
    piece_linear = PieceLinear(samples)
    piece_linear.interp()
    other_samples = point.random_sample(5, a, b, c, d, e, f)
    for i in range(len(other_samples)):
        y = piece_linear.cal(other_samples[i].x)
        err = abs(y - other_samples[i].y)
        print("插值法计算的结果为：{}, 原函数计算的结果为: {}, 误差为: {}".format(y, other_samples[i].y, err))
    drawer = Drawer()
    drawer.draw_interp(a, b, c, d, e, f, piece_linear.vector_cal, 'Piecewise Linear Method')


def test_hermite():
    print("分段三次 Hermite 插值法")
    npoints = 1000
    a = 0 
    b = 5
    c = 1
    d = 1
    e = 1
    f = 1
    samples = point.fixed_sample(npoints, a, b, c, d, e, f)
    for i in range(0, len(samples)):
        d = point.point_derivative(samples[i].x, c, d, e, f)
        samples[i].derivative(d)
        # print("导数为: {}".format(d))
    hermite = Hermite(samples)
    hermite.interp()
    other_samples = point.random_sample(5, a, b, c, d, e, f)
    for i in range(len(other_samples)):
        y = hermite.cal(other_samples[i].x)
        err = abs(y - other_samples[i].y)
        print("插值法计算的结果为：{}, 原函数计算的结果为: {}, 误差为: {}".format(y, other_samples[i].y, err))
    drawer = Drawer()
    drawer.draw_interp(a, b, c, d, e, f, hermite.vector_cal, 'Cubic Hermite Method')


def test_best_square(a: float, b: float, c: int, k: int, n: int):
    best_square = BestSquare(k, a, b, c)
    # best_square.fit()
    best_square.legrand_fit()
    samples = point.random_x(a, b, n)
    target_fn = TargetFn(a, b, c)
    for sample in samples:
        std_val = target_fn.fn(sample, False)
        app_val = best_square.cal(((1 / (b - a)) * (2 * sample - a - b)))
        # app_val = best_square.cal(sample)
        # app_val = best_square.cal((b - a) * sample + a + b)
        err = abs(std_val - app_val)
        print("标准函数计算的结果为：{}, 逼近函数计算的结果为: {}, 误差为: {}".format(std_val, app_val, err))
    drawer = Drawer()
    drawer.legendre_cmp_draw(a, b, target_fn.fn, best_square.cal, 'Best Square Method(k = 3)')
    # drawer.cmp_draw(a, b, target_fn.fn, best_square.cal, 'Best Square Method')

def test_least_square(a: float, b: float, c: int, n: int, k: int):
    samples = point.approx_fixed_sample(n, a, b, c)
    target_fn = TargetFn(a, b, c)
    least_square = LeastSquare(a, b, c, k, samples)
    least_square.fit()
    other_samples = point.approx_random_sample(10, a, b, c)
    for sample in other_samples:
        std_val = sample.y
        app_val = least_square.cal(sample.x)
        err = abs(std_val - app_val)
        print("标准函数计算的结果为：{}, 逼近函数计算的结果为: {}, 误差为: {}".format(std_val, app_val, err))
    drawer = Drawer()
    drawer.cmp_draw(a, b, target_fn.normal_fn, least_square.cal, 'Least Square Method(k = 3)')


# 复化梯形公式
def test_trapezodial(a: float, b: float, delta: float):
    i = 1
    while True:
        h = (b - a)/ pow(2, i)
        integrate = trapezodial(a, b, h)
        std_integrate = stdintegrate(a, b)
        err = abs(integrate - std_integrate)
        if err < delta: 
            print("标准函数积分值为: {}, 数值积分值为: {}, 误差为: {}".format(std_integrate, integrate, err))
            print("此时被分成 {} 等份, h = {}".format(pow(2, i), h))
            return 
        i += 1

# 龙贝格积分测试
def test_romberg(a: float, b: float, delta: float):
    romberg(a, b, delta)

def test_gaussian_elimination():
    A = np.array([
        [31, -13, 0, 0, 0, -10, 0, 0, 0 ],
        [-13, 35, -9, 0, -11, 0, 0, 0, 0],
        [0.0, -9, 31, -10, 0, 0, 0, 0, 0],
        [0, 0, -10, 79, -30, 0, 0, 0, -9],
        [0, 0, 0, -30, 57, -7, 0, -5, 0 ],
        [0, 0, 0, 0, -7, 47, -30 , 0, 0 ],
        [0, 0, 0, 0, 0, -30, 41, 0, 0   ],
        [0, 0, 0, 0, -5, 0, 0, 27, -2   ],
        [0, 0, 0, -9, 0, 0, 0, -2, 29   ],
    ])
    B = np.array([-15.0, 27, -23, 0, -20, 12, -7, 7, 10])
    matrix = Matrix(A, B)
    ans = matrix.slove()
    count = matrix.gaussian_slove()
    print("正确结果为: {}".format(ans))
    print("使用高斯消元法计算出的结果为: {}".format(count))


def example():
    # test_vandermonde()
    # test_lagrange()
    # test_newton()
    # test_piecelinear()
    # test_hermite()
    # test_best_square(1, 5, 1, 3, 10)
    # test_least_square(1, 5, 1, 100, 3)
    # test_trapezodial(1, 5, 0.0001)
    # test_romberg(1, 5, 0.0001)
    test_gaussian_elimination()

if __name__ == '__main__':
    example()