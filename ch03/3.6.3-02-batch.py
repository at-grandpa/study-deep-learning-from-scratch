import sys, os, pickle
sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from lib import common as c
from lib import softmax as soft
from lib import sigmoid as sig


def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("ch03/sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = c.np.dot(x, W1) + b1
    z1 = sig.sigmoid(a1)
    a2 = c.np.dot(z1, W2) + b2
    z2 = sig.sigmoid(a2)
    a3 = c.np.dot(z2, W3) + b3
    y = soft.softmax(a3)

    return y

x, t = get_data()
network = init_network()

batch_size = 100
accuracy_count = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = c.np.argmax(y_batch, axis=1)
    accuracy_count += c.np.sum(p == t[i:i+batch_size])

print("Accuracy:" + str(float(accuracy_count) / len(x)))

