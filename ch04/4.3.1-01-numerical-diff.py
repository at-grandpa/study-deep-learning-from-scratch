import sys, os, pickle
sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from lib import common as c

def numerical_diff(f, x) :
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2 * h)

def function_1(x) :
    return 0.01*x**2 + 0.1*x

x = c.np.arange(0.0, 20.0, 0.1)
y = function_1(x)

c.plt.xlabel("x")
c.plt.ylabel("f(x)")

c.plt.plot(x, y)
c.plt_show_alt(c.plt)

print(numerical_diff(function_1, 5))

