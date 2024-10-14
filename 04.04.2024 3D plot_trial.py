# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 22:56:14 2024

@author: Dell
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from scipy import stats

X = [ 507, 1100, 1105, 1080, 378, 398, 373]
Y = [1047,  838,  821,  838, 644, 644, 659]
Z = [ 300,   55,   15,   15,  55,  15,  15]

kernel = stats.gaussian_kde(np.array([X, Y]), weights=Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
xs, ys = np.mgrid[0:1500:30j, 0:1500:30j]
zs = kernel(np.array([xs.ravel(), ys.ravel()])).reshape(xs.shape)
ax.plot_surface(xs, ys, zs, cmap="hot_r", lw=0.5, rstride=1, cstride=1, ec='k')
plt.show()

