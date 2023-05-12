# -*- coding: utf-8 -*-
"""
Created on Fri May 12 10:28:52 2023

@author: Yiteng Tang
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Set the path to the CSV file
file_path = r'E:\XRD\2023\5\05082023\12272021PbSClNPL_2.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Assuming the first column is x and the second column is y
x = df.iloc[:, 0]
y = df.iloc[:, 1]

# Set a prominence threshold to ignore small peaks
prominence_threshold = 50

# Detect the peaks in the data with a prominence threshold
peaks, _ = find_peaks(y, prominence=prominence_threshold)

# Create a figure with a specified size (width, height) in inches and dpi
plt.figure(figsize=(10, 6), dpi=100)

# Plot the data as a line graph with a linewidth of 3
plt.plot(x, y, linewidth=3)

# Plot the detected peaks
plt.plot(x[peaks], y[peaks], 'ro', markersize=5)

# Annotate the peaks with their x and y values
for peak in peaks:
    plt.annotate(f'({x[peak]:.2f}, {y[peak]:.2f})', 
                 (x[peak], y[peak]), textcoords="offset points", 
                 xytext=(-10,5), ha='center', fontsize=12, color='red')

# Set the x-axis label to "2θ" using the Greek letter theta

plt.xlabel('2θ', fontsize =16)
plt.ylabel('Counts', fontsize =16)
plt.title('PbSCl NPL', fontsize =16)

# Set the tick labels to be inside the plot
plt.tick_params(axis='both', direction='in', labelsize = 16)

# Show the plot
plt.show()

