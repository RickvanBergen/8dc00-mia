# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 12:22:43 2019

@author: 20174099
"""

import numpy as np
import matplotlib.pyplot as plt
import registration as reg
import registration_util as util
from scipy import ndimage
from IPython.display import display, clear_output

p=2
x=np.zeros([2,2])
for i in range(2):
    x[1,i]=1
print(x)