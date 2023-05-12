

# -*- coding: utf-8 -*-
"""
Created on Fri May 12 11:44:17 2023

@author: Yiteng Tang
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Function to remove commas from a string
def remove_comma(s):
    return float(s.replace(',', ''))

# Set the path to the text file
file_path = r'E:\XRD\2023\mki\Yitang sample from 30-50 degree time 30 s.txt'

# Read the text file (assuming space or tab delimiter), skipping the first line ([Data]) and column names (Angle, PSD)
# Remove commas from the values using the remove_comma function
df = pd.read_csv(file_path, delim_whitespace=True, header=None, skiprows=161, skipinitialspace=True, converters={0: remove_comma, 1: remove_comma})

# Assuming the first column is x and the second column is y
x = df.iloc[:, 0]
y = df.iloc[:, 1]

# Set a prominence threshold to ignore small peaks
prominence_threshold = 500

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
    
# Add shorter vertical drop lines at specific x-axis values
drop_line_positions = [24.7,29.8,42.7]
drop_line_height = 1000  # Customize the height of the drop lines
for position in drop_line_positions:
    plt.plot([position, position], [0, drop_line_height], color='blue', linestyle='--', linewidth=1)


# Set the x-axis label to "2θ" using the Greek letter theta

plt.xlabel('2θ', fontsize =16)
plt.ylabel('Counts', fontsize =16)
plt.title('PbSCl NPL', fontsize =16)

# Set the y-axis range starting from 0
plt.ylim(0, max(y) + 500)
plt.xlim(20,51)

# Set the tick labels to be inside the plot
plt.tick_params(axis='both', direction='in', labelsize = 16)

# Show the plot
plt.show()

