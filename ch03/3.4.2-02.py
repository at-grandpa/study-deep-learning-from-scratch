from lib import common as c
from lib import sigmoid as sig

def identity_function(x):
    return x

def init_network():
    network = {}
    network['W1'] = c.np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = c.np.array([0.1, 0.2, 0.3])
    network['W2'] = c.np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = c.np.array([0.1, 0.2])
    network['W3'] = c.np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = c.np.array([0.1, 0.2])

    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = c.np.dot(x, W1) + b1
    z1 = sig.sigmoid(a1)
    a2 = c.np.dot(z1, W2) + b2
    z2 = sig.sigmoid(a2)
    a3 = c.np.dot(z2, W3) + b3
    Y  = identity_function(a3)

    return Y


network = init_network()
x = c.np.array([1.0, 0.5])
y = forward(network, x)

print(y)

