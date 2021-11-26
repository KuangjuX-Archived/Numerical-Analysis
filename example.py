import numpy as np
import interp
from draw import Drawer
from interp.hermite import Hermite
from interp.lagrange import Largrange
from interp.newton import Netwon
from interp.piece_linear import PieceLinear
from interp.vandermonde import Vandermonde

def test_vandermonde():
    print("范德蒙德插值法")
    npoints = 10
    a = 0
    b = 5
    c = 1
    d = 1
    e = 1
    f = 1
    samples = interp.random_sample(npoints, a, b, c, d, e, f)
    vandermonde = Vandermonde(samples)
    fn = vandermonde.interp()
    other_samples = interp.random_sample(5, a, b, c, d, e, f)
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
    samples = interp.random_sample(npoints, a, b, c, d, e, f)
    newton = Netwon(samples)
    fn = newton.interp()
    other_samples = interp.random_sample(5, a, b, c, d, e, f)
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
    samples = interp.random_sample(npoints, a, b, c, d, e, f)
    lagrange = Largrange(samples)
    fn = lagrange.interp()
    other_samples = interp.random_sample(5, a, b, c, d, e, f)
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
    samples = interp.fixed_sample(npoints, a, b, c, d, e, f)
    piece_linear = PieceLinear(samples)
    piece_linear.interp()
    other_samples = interp.random_sample(5, a, b, c, d, e, f)
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
    samples = interp.fixed_sample(npoints, a, b, c, d, e, f)
    for i in range(0, len(samples)):
        d = interp.point_derivative(samples[i].x, c, d, e, f)
        samples[i].derivative(d)
        # print("导数为: {}".format(d))
    hermite = Hermite(samples)
    hermite.interp()
    other_samples = interp.random_sample(5, a, b, c, d, e, f)
    for i in range(len(other_samples)):
        y = hermite.cal(other_samples[i].x)
        err = abs(y - other_samples[i].y)
        print("插值法计算的结果为：{}, 原函数计算的结果为: {}, 误差为: {}".format(y, other_samples[i].y, err))
    drawer = Drawer()
    drawer.draw_interp(a, b, c, d, e, f, hermite.vector_cal, 'Cubic Hermite Method')



def example():
    test_vandermonde()
    test_lagrange()
    test_newton()
    test_piecelinear()
    test_hermite()

if __name__ == '__main__':
    example()