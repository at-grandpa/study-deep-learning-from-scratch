from lib import common as c

x = c.np.arange(0, 6, 0.1)
y = c.np.sin(x)

c.plt.plot(x, y)
c.plt_show_alt(c.plt)
