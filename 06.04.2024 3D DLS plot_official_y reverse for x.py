# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 16:06:03 2024

@author: Dell
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.stats import gaussian_kde

Y = [0.621, 0.621, 0.72, 0.62, 1.74, 0.965, 1.5, 2.01, 0.72, 4.85]
X = [10, 20, 30, 40, 40, 50, 60, 70, 80, 80]
Z = [37.1, 32.3, 30.2, 35.1, 19.4, 21.9, 22, 18.1, 20.8, 19.3]

# Check if dimensions of X, Y, and Z match
if len(X) != len(Y) or len(X) != len(Z):
    raise ValueError("The dimensions of X, Y, and Z must match.")

# Create 3D KDE
data = np.vstack([X, Y])
kde = gaussian_kde(data, weights=Z)

# Define grid for plotting
x_min, x_max = min(X), max(X)
y_min, y_max = min(Y), max(Y)
x_grid, y_grid = np.meshgrid(np.linspace(x_min, x_max, 30),
                             np.linspace(y_min, y_max, 30))

# Evaluate KDE on grid
positions = np.vstack([x_grid.ravel(), y_grid.ravel()])
densities = kde(positions).reshape(x_grid.shape)

# Plot 3D surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, densities, cmap='viridis', edgecolor='none')

# Set axis labels
ax.set_xlabel('Glycerol, %', fontsize=10, fontweight='bold', labelpad=2)
ax.set_ylabel('Size, nm', fontsize=10, fontweight='bold', labelpad=0.1)
ax.set_zlabel('KDE', fontsize=10, fontweight='bold', labelpad=0.1, rotation = 0)

# Adjust size and boldness of axis values (ticks)
ax.tick_params(axis='x', labelsize=8, pad=0.05, width=2, labelcolor='black', labelrotation=45, grid_alpha=0.5, grid_linewidth=1)
ax.tick_params(axis='y', labelsize=8, pad=0.1, width=2, labelcolor='black', labelrotation=45, grid_alpha=0.5, grid_linewidth=1)
ax.tick_params(axis='z', labelsize=8, pad=6, width=2, labelcolor='black', labelrotation=0, grid_alpha=0.5, grid_linewidth=1)

# Set the bounds of the y-axis
ax.set_ylim(0, 5)

# Set the bounds of the x-axis
ax.set_xlim(0, 80)

# Set the bounds of the z-axis
ax.set_zlim(0, 0.006)

# Set major units of the z-axis
ax.zaxis.set_major_locator(plt.MultipleLocator(0.002))

# Add a title
ax.set_title('3D KDE Plot', fontsize=12, fontweight='bold', pad=1)

# Move z-axis title up by setting position to 0
ax.zaxis.set_label_coords(0, 0)

plt.show()


