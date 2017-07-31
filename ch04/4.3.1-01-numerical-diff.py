import sys, os, pickle
sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from lib import common as c

def numerical_diff(f, x) :
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2 * h)

def function_1(x) :
    return 0.01*x**2 + 0.1*x

def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

x = c.np.arange(0.0, 20.0, 0.1)
y = function_1(x)

c.plt.xlabel("x")
c.plt.ylabel("f(x)")


# Point
x_point = 15

# Calculate
tf = tangent_line(function_1, x_point)
y2 = tf(x)

# Range
c.plt.xlim(0, 20)
c.plt.ylim(-1, 6)

# Dashed line
c.plt.plot([0, x_point], [function_1(x_point), function_1(x_point)], '--o')
c.plt.plot([x_point, x_point], [-1, function_1(x_point)], '--o')

# Graph
c.plt.plot(x, y)
c.plt.plot(x, y2)
c.plt_show_alt(c.plt)

print(numerical_diff(function_1, 5))

