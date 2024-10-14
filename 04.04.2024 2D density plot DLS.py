# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from the CSV file
data = pd.read_csv('DLS map plot.csv')

# Specify the common x variable and different y variables
x_variable = 'Volume_dstr'
y_variables = ['2-80%', '5-80%', '70%', '60%', '50%', '1-40%', '30%']  # Add more as needed

# Create a single figure for the plot
plt.figure(figsize=(10, 6))

# Plot each y variable as a separate kernel density plot
for y_var in y_variables:
    sns.kdeplot(data=data, x=x_variable, y=y_var, label=y_var)
    plt.xlim(-7, 20)
    plt.ylim(-10, 25)

# Add labels and title
plt.xlabel('Size_nm')
plt.ylabel('Volume_dstr')
plt.title('2D plot of fractional size distribution')

# Add legend
plt.legend()

# Show the plot
plt.show()


