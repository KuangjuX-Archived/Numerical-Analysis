import interp
from interp.lagrange import Largrange
from interp.newton import Netwon
from interp.vandermonde import Vandermonde

def test_vandermonde():
    samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    # func = interp.vandermonde(samples, 10)
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




def example():
    # test_newton()
    test_lagrange()
    # test_vandermonde()

if __name__ == '__main__':
    example()