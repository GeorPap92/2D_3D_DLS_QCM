# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 13:41:10 2024

@author: Dell
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
from scipy import stats
from matplotlib.ticker import FuncFormatter

X = [0.621, 0.621, 0.72, 0.62, 1.74, 0.965, 1.5, 2.01, 0.72, 4.85]
Y = [10, 20, 30, 40, 40, 50, 60, 70, 80, 80]
Z = [37.1, 32.3, 30.2, 35.1, 19.4, 21.9, 22, 18.1, 20.8, 19.3]

kernel = stats.gaussian_kde(np.array([X, Y]), weights=Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Plot the surface
xs, ys = np.mgrid[0:5:30j, 0:100:30j]
zs = kernel(np.array([xs.ravel(), ys.ravel()])).reshape(xs.shape)
surf = ax.plot_surface(xs, ys, zs, cmap="viridis", lw=0.5, rstride=1, cstride=1, ec='k')

# Set axis labels with bold font and size
ax.set_xlabel('Size, nm', fontsize=10, fontweight='bold', labelpad=0.1)
ax.set_ylabel('Glycerol, %', fontsize=10, fontweight='bold', labelpad=0.1)
ax.set_zlabel('KDE', fontsize=10, fontweight='bold', labelpad=0.05, rotation =0)


# Set the bounds of the y-axis
ax.set_ylim(0, 80)


# Set major units of the y-axis
ax.yaxis.set_major_locator(plt.MultipleLocator(20))

# Adjust size and boldness of axis values (ticks)
ax.tick_params(axis='x', labelsize=8, pad=0.05, width=2, labelcolor='black', labelrotation=45, grid_alpha=0.5, grid_linewidth=1)
ax.tick_params(axis='y', labelsize=8, pad=0.1, width=2, labelcolor='black', labelrotation=45, grid_alpha=0.5, grid_linewidth=1)
ax.tick_params(axis='z', labelsize=8, pad=5, width=2, labelcolor='black', labelrotation=0, grid_alpha=0.5, grid_linewidth=1)

# Set z-axis tick locations
ax.set_zticks([0.00, 0.005])

# Set major units of the z-axis
ax.zaxis.set_major_locator(plt.MultipleLocator(0.0025))

# Manually format z-axis tick labels
def format_z_tick(value, pos):
    return f"{value:.2e}"

ax.zaxis.set_major_formatter(FuncFormatter(format_z_tick))

# Add a title
ax.set_title('3D KDE Plot', fontsize=12, fontweight='bold', pad=1)

plt.show()
