from common import lib as l
from matplotlib.image import imread

def NAND(x1, x2):
    x = l.np.array([x1, x2])
    w = l.np.array([-0.5, -0.5])
    b = 0.7
    tmp = l.np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print("(0, 0) => " + str(NAND(0, 0)) )
print("(0, 1) => " + str(NAND(0, 1)) )
print("(1, 0) => " + str(NAND(1, 0)) )
print("(1, 1) => " + str(NAND(1, 1)) )
