from subprocess import *

import random, math, sys, os

import numpy as np
import matplotlib as mpl
mpl.use('Agg')
from matplotlib import pyplot as plt

def plt_show_alt(plt):
    plt.savefig("/tmp/output.png")
    process = Popen(["/usr/local/bin/imgcat", "/tmp/output.png"])
    plt.clf()
