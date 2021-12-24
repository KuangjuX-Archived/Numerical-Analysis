from scipy.misc import derivative

class NonLinear:
    def __init__(self, fn):
        self.fn = fn
    
    # 不动点迭代, x0 为初始点, delta 为要求的误差值
    def fixed_iter(self, x0, delta):
        x = x0
        y = x0
        count = 0
        while True:
            y = self.fn(x)
            print("x: {}, y: {}".format(x, y))
            err = abs(x - y)
            if err < delta:
                break
            else:
                x = y
            count += 1
        return (y, count)
    
    # 斯蒂芬森迭代法
    def stefenson_iter(self, x0, delta):
        x = x0
        y = x0
        z = x0
        next_x = x0
        count = 0
        while True:
            y = self.fn(x)
            z = self.fn(y)
            next_x = x - ((y - x)*(y - x) / (z - 2*y +x))
            err = abs(next_x - x)
            if err < delta:
                break
            else:
                x = next_x
            count += 1
        return (next_x, count)

    # 牛顿迭代法
    def newton_iter(self, x0, delta):
        x = x0
        next_x = x0
        count = 0
        while True:
            next_x = x - (self.fn(x)/derivative(self.fn, x))
            err = abs(next_x - x)
            if err < delta:
                break 
            else: 
                x = next_x
            count += 1
        return (next_x, count)