from lib import common as c

def step_function(x):
    return c.np.array(x > 0, dtype = c.np.int)

x = c.np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
c.plt.plot(x, y)
c.plt_show_alt(c.plt)

