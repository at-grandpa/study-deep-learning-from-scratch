from lib import common as c

def softmax(a):
    m = c.np.max(a)
    exp_a = c.np.exp(a - m)
    sum_exp_a = c.np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

