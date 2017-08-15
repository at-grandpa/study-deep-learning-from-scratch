# coding: utf-8
from mpl_toolkits.mplot3d import Axes3D

import sys, os, pickle
sys.path.append(os.pardir)

from lib import common as c

from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class simpleNet:
    def __init__(self):
        self.W = c.np.random.randn(2,3)

    def predict(self, x):
        return c.np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss

x = c.np.array([0.6, 0.9])
t = c.np.array([0, 0, 1])

net = simpleNet()

f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)

print(dW)
