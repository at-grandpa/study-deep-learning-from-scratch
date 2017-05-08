from common import lib as l
from matplotlib.image import imread

def OR(x1, x2):
    x = l.np.array([x1, x2])
    w = l.np.array([0.5, 0.5])
    b = -0.2
    tmp = l.np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("(0, 0) => " + str(OR(0, 0)) )
print("(0, 1) => " + str(OR(0, 1)) )
print("(1, 0) => " + str(OR(1, 0)) )
print("(1, 1) => " + str(OR(1, 1)) )
