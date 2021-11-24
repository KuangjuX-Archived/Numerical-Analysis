from random import sample
import interp
from interp.hermite import Hermite
from interp.lagrange import Largrange
from interp.newton import Netwon
from interp.piece_linear import PieceLinear
from interp.vandermonde import Vandermonde

def test_vandermonde():
    samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    vandermonde = Vandermonde(samples)
    fn = vandermonde.interp()
    other_samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    interp.point_test(fn, other_samples)

def test_newton():
    samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    newton = Netwon(samples)
    fn = newton.interp()
    other_samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    interp.point_test(fn, other_samples)

def test_lagrange():
    samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    lagrange = Largrange(samples)
    fn = lagrange.interp()
    other_samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    interp.point_test(fn, other_samples)

def test_piecelinear():
    samples = interp.fixed_sample(1000, 1, 5, 1, 1, 1, 1)
    piece_linear = PieceLinear(samples)
    piece_linear.interp()
    other_samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    for i in range(len(other_samples)):
        y = piece_linear.cal(other_samples[i].x)
        err = abs(y - other_samples[i].y)
        print("插值法计算的结果为：{}, 原函数计算的结果为: {}, 误差为: {}".format(y, other_samples[i].y, err))


def test_hermite():
    c = 1
    d = 1
    e = 1
    f = 1
    samples = interp.fixed_sample(1000, 1, 5, c, d, e, f)
    for i in range(0, len(samples)):
        d = interp.point_derivative(samples[i].x, c, d, e, f)
        samples[i].derivative(d)
        # print("导数为: {}".format(d))
    hermite = Hermite(samples)
    hermite.interp()
    other_samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    for i in range(len(other_samples)):
        y = hermite.cal(other_samples[i].x)
        err = abs(y - other_samples[i].y)
        print("插值法计算的结果为：{}, 原函数计算的结果为: {}, 误差为: {}".format(y, other_samples[i].y, err))



def example():
    # test_newton()
    # test_lagrange()
    # test_vandermonde()
    # test_piecelinear()
    test_hermite()

if __name__ == '__main__':
    example()