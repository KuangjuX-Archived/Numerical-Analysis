import matplotlib.pyplot as plt
import numpy as np

class Drawer:
    def __init__(self):
        pass

    def cmp_draw(self, a: float, b: float, f1, f2, title: str):
        # 给定任意函数的表达式，画出它们的图像对比
        x = np.linspace(a, b, 100)
        y1 = [f1(item) for item in x]
        y2 = [f2(item) for item in x]
        fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True)
        ax1.plot(x, y1, label = 'True CUrve', color = 'red')
        ax1.legend()
        ax2.plot(x, y2, label = 'Approx Curve', color = 'green')
        ax2.legend()
        fig.suptitle(title)
        plt.savefig('image/{}.png'.format(title))

    def draw_interp(self, a: float, b: float, c: float, d: float, e: float, f: float, fn, title: str):
        x = np.linspace(a, b, 100)
        y1 = c * np.sin(d * x) + e * np.cos(f * x)
        y2 = fn(x)
        fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True)
        ax1.plot(x, y1, label = 'True Curve', color = 'red')
        ax1.legend()
        ax2.plot(x, y2, label = 'Interp Curve', color = 'green')
        ax2.legend()
        fig.suptitle(title)
        plt.savefig('image/{}.png'.format(title))
