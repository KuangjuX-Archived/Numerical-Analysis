import interp

def example():
    samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    func = interp.vandermonde(samples, 10)
    other_samples = interp.point_sample(10, 1, 5, 1, 1, 1, 1)
    interp.point_test(func, other_samples)

if __name__ == '__main__':
    example()