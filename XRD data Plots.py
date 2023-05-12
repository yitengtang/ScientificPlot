# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:12:49 2023

@author: Yiteng Tang
"""

import pandas as pd
import matplotlib.pyplot as plt

# Set the path to the CSV file
file_path = r'E:\XRD\2023\5\05082023\12272021PbSClNPL_4.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Assuming the first column is x and the second column is y
x = df.iloc[:, 0]
y = df.iloc[:, 1]

# Create a figure with a specified size (width, height) in inches and dpi
plt.figure(figsize=(10, 6), dpi=100)

# Plot the data as a line graph with a linewidth of 3
plt.plot(x, y, linewidth=3)
plt.xlabel('2θ', fontsize =16)
plt.ylabel('Counts', fontsize =16)
plt.title('PbSCl NPL', fontsize =16)

# Set the tick labels to be inside the plot
plt.tick_params(axis='both', direction='in', labelsize = 16)

# Show the plot
plt.show()
