import sys, os
sys.path.append(os.pardir)

from dataset.mnist import load_mnist
from lib import common as c

(x_train, t_train), (x_test, t_test) = \
        load_mnist(flatten=True, one_hot_label=True, normalize=False)

img = x_train[0]
label = t_train[0]

print(label)
print(img.shape)

img = img.reshape(28, 28)
print(img.shape)

c.image_show_alt(img)
