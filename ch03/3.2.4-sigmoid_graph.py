from lib import common as c

def sigmoid(x):
    return 1 / (1 + c.np.exp(-x))

x = c.np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
c.plt.plot(x, y)
c.plt_show_alt(c.plt)

