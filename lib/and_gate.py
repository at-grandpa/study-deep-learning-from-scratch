from . import common as c

def AND(x1, x2):
    x = c.np.array([x1, x2])
    w = c.np.array([0.5, 0.5])
    b = -0.7
    tmp = c.np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
