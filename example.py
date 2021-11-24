import interp
from interp.newton import Netwon

def test_vandermonde():
    samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    func = interp.vandermonde(samples, 10)
    other_samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    interp.point_test(func, other_samples)

def test_newton():
    samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    newton = Netwon(samples)
    fn = newton.netwon()
    other_samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    interp.point_test(fn, other_samples)



def example():
    test_newton()

if __name__ == '__main__':
    example()