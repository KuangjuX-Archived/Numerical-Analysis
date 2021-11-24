import matplotlib.pyplot as plt
import numpy as np

def draw_trig(a: float, b: float, c: float, d: float, e: float, f: float):
    x = np.linspace(a, b, 30)
    y = c * np.sin(d * x) + e * np.cos(f * x)
    plt.plot(x, y)
    plt.show()


def draw_poly(fn, a: float, b: float):
    x = np.linspace(a, b, 30)
    y = fn(x)
    plt.plot(x, y)
    plt.show()