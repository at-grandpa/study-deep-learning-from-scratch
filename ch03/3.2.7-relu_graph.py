from lib import common as c

def relu(x):
    return c.np.maximum(0, x)

x = c.np.arange(-5.0, 5.0, 0.1)
y = relu(x)
c.plt.plot(x, y)
c.plt.ylim(-0.1, 5.1)
c.plt_show_alt(c.plt)

