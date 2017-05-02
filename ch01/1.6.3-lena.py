from common import lib as l
from matplotlib.image import imread

current_dir_path = l.os.path.dirname(__file__)
img = imread(current_dir_path + '/../dataset/lena.png')
l.plt.imshow(img)
l.plt_show_alt(l.plt)
