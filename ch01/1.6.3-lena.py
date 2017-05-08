from lib import common as c
from matplotlib.image import imread

current_dir_path = c.os.path.dirname(__file__)
img = imread(current_dir_path + '/../dataset/lena.png')
c.plt.imshow(img)
c.plt_show_alt(c.plt)
