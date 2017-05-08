from common import lib as l
from matplotlib.image import imread

def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print("(0, 0) => " + str(AND(0, 0)) )
print("(0, 1) => " + str(AND(0, 1)) )
print("(1, 0) => " + str(AND(1, 0)) )
print("(1, 1) => " + str(AND(1, 1)) )
