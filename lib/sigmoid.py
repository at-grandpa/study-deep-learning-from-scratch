from lib import common as c

def sigmoid(x):
    return 1 / (1 + c.np.exp(-x))
