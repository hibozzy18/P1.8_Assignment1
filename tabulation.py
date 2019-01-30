""" The script is used to plot variables of x against  variables 
of y """
from __future__ import print_function
import sys

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib import pylab as pl
import numpy as np

xval = [x for x in pl.frange(-5.0, 5.0, 0.1)]
if(len(sys.argv) == 2):
    option = sys.argv[1]
    if(int(option) == 1):
    	yval = [x for x in xval]    
    elif(int(option) == 2):
    	yval = [x**2 for x in xval]
    elif(int(option) == 3):
        yval = [x**3 for x in xval]
    
else:
	pass

plt.plot(xval, yval)
plt.show()