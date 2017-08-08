from mpl_toolkits.mplot3d import Axes3D

import sys, os, pickle
sys.path.append(os.pardir)

from lib import common as c

def numerical_diff(f, x) :
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2 * h)

def function_2(x) :
    return x[0]**2 + x[1]**1

#def function_2(x):
#    if x.ndim == 1:
#        return c.np.sum(x**2)
#    else:
#        return c.np.sum(x**2, axis=1)

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

def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    x_history = []

    for i in range(step_num):
        x_history.append( x.copy() )

        grad = numerical_gradient(f, x)
        x -= lr * grad

    return x, c.np.array(x_history)

init_x = c.np.array([-3.0, 4.0])
print(gradient_descent(function_2, init_x=init_x, lr=0.1, step_num=100))

init_x = c.np.array([-3.0, 4.0])

lr = 0.1
step_num = 20
x, x_history = gradient_descent(function_2, init_x, lr=lr, step_num=step_num)

c.plt.plot( [-5, 5], [0,0], '--b')
c.plt.plot( [0,0], [-5, 5], '--b')
c.plt.plot(x_history[:,0], x_history[:,1], 'o')

c.plt.xlim(-3.5, 3.5)
c.plt.ylim(-4.5, 4.5)
c.plt.xlabel("X0")
c.plt.ylabel("X1")


c.plt_show_alt(c.plt)
