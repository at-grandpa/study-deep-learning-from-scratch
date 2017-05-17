from lib import common as c

def step_function(x):
    y = x > 0
    return y.astype(c.np.int)

print(step_function(c.np.array([-1.0, 1.0, 2.0])))

