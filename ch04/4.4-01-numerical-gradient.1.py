from mpl_toolkits.mplot3d import Axes3D

import sys, os, pickle
sys.path.append(os.pardir)

from lib import common as c

def numerical_diff(f, x) :
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2 * h)

#def function_2(x) :
#    return x[0]**2 + x[1]**2

def function_2(x):
    if x.ndim == 1:
        return c.np.sum(x**2)
    else:
        return c.np.sum(x**2, axis=1)

def tangent_line(f, x):
    d = numerical_diff(f, x)
    print(d)
    y = f(x) - d*x
    return lambda t: d*t + y

def _numerical_gradient_no_batch(f, x):
    h = 1e-4 # 0.0001
    grad = c.np.zeros_like(x) # xと同じ形状の配列を生成

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)の計算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)の計算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val
        
    return grad

def numerical_gradient(f, X):
    if X.ndim == 1:
        return _numerical_gradient_no_batch(f, X)
    else:
        grad = c.np.zeros_like(X)

        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_no_batch(f, x)

        return grad

x0 = c.np.arange(-2, 2.5, 0.25)
x1 = c.np.arange(-2, 2.5, 0.25)
X, Y = c.np.meshgrid(x0, x1)
X = X.flatten()
Y = Y.flatten()
grad = numerical_gradient(function_2, c.np.array([X, Y]) )
c.plt.figure()
c.plt.quiver(X, Y, -grad[0], -grad[1],  angles="xy",color="#666666", label='4.4')#,headwidth=10,scale=40,color="#444444")
c.plt.xlim([-2, 2])
c.plt.ylim([-2, 2])
c.plt.xlabel('x0')
c.plt.ylabel('x1')
c.plt.grid()
c.plt.legend()
c.plt.draw()

c.plt_show_alt(c.plt)
