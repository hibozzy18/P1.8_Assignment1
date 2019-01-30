""" The script is used to plot variables of x against  variables 
of y """
from __future__ import print_function
import sys

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import pylab as pl
import numpy as np

xval = [x for x in pl.frange(-3.0, 3.0, 0.1)]
if(len(sys.argv) == 2):
    option = sys.argv[1]
    if(int(option) == 1):
    	yval = [x for x in xval]
    	pass
else:
	print(""""
    Wrong argument list!!. 
    Usage:Tabulation.py N where N is a number between from 1 to 8 inclusive.\n
    N has the following options:
    1 ---   f(x) 
    """)
    sys.exit(1)

plt.plot(xval, yval)
plt.show()