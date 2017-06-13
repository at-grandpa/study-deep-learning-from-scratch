from lib import common as c
from lib import softmax as soft

a = c.np.array([0.3, 2.9, 4.0])
y = soft.softmax(a)

print(y)
print(c.np.sum(y))

