# coding: utf-8
from mpl_toolkits.mplot3d import Axes3D

import sys
import os
import pickle
sys.path.append(os.pardir)

from lib import common as c

from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient


class TwoLayerNet:

    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 重みの初期化
        self.params = {}
        self.params['W1'] = weight_init_std * \
            c.np.random.randn(input_size, hidden_size)
        self.params['b1'] = c.np.zeros(hidden_size)
        self.params['W2'] = weight_init_std * \
            c.np.random.randn(hidden_size, output_size)
        self.params['b2'] = c.np.zeros(output_size)

    def predict(self, x):
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']

        a1 = c.np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = c.np.dot(z1, W2) + b2
        y = softmax(a2)

        return y

    def loss(self, x, t):
        y = self.predict(x)

        return cross_entropy_error(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = c.np.argmax(y, axis=1)
        t = c.np.argmax(t, axis=1)

        accuracy = c.np.sum(y == t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        def loss_W(W): return self.loss(x, t)

        grads = {}
        grads['W1'] = numerical_gradient(loss_W, self.params['W1'])
        grads['b1'] = numerical_gradient(loss_W, self.params['b1'])
        grads['W2'] = numerical_gradient(loss_W, self.params['W2'])
        grads['b2'] = numerical_gradient(loss_W, self.params['b2'])
        return grads

net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)

print(net.params['W1'].shape)
print(net.params['b1'].shape)
print(net.params['W2'].shape)
print(net.params['b2'].shape)