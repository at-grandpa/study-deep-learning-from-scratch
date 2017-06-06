from lib import common as c
from lib import sigmoid as sig

X = c.np.array([1.0, 0.5])
W1 = c.np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = c.np.array([0.1, 0.2, 0.3])
print(X.shape)
print(W1.shape)
print(B1.shape)

A1 = c.np.dot(X, W1) + B1
print(A1)

Z1 = sig.sigmoid(A1)
W2 = c.np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = c.np.array([0.1, 0.2])

print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = c.np.dot(Z1, W2) + B2
print(A2)

Z2 = sig.sigmoid(A2)
print(Z2)

def identity_function(x):
    return x

W3 = c.np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = c.np.array([0.1, 0.2])

A3 = c.np.dot(Z2, W3) + B3
Y = identity_function(A3)

print(Y)
