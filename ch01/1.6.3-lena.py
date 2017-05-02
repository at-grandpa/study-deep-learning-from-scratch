from common import lib as l
from matplotlib.image import imread

img = imread('../dataset/lena.png')
l.plt.imshow(img)
l.plt_show_alt(l.plt)
