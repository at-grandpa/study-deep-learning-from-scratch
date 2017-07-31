from mpl_toolkits.mplot3d import Axes3D

import sys, os, pickle
sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from lib import common as c

def numerical_diff(f, x) :
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2 * h)

def function_2(x) :
    return x[0]**2 + x[1]**2

def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

x = c.np.arange(-3.0, 3.0, 0.1)
y = c.np.arange(-3.0, 3.0, 0.1)
X, Y = c.np.meshgrid(x, y)
Z = function_2(c.np.array([X, Y]))

fig = c.plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X,Y,Z)

c.plt_show_alt(c.plt)
