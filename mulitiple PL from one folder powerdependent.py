# -*- coding: utf-8 -*-
"""
Created on Tue May 16 11:11:31 2023

@author: T3139
"""

import matplotlib.pyplot as plt
import glob
import os
import re

# Path to the folder containing the text files
folder_path = r'E:\PL\2023\5\npl\New folder'

# Get a list of all the text files in the folder
file_list = glob.glob(folder_path + '/*.txt')

# Sort the file list numerically
file_list.sort(key=lambda x: [float(s) if s.isdigit() else s.lower() for s in re.split(r'(\d+)', os.path.splitext(os.path.basename(x))[0])])

# Create a figure with a specified size (width, height) in inches and dpi
plt.figure(figsize=(10, 6), dpi=100)

# Iterate over each file and plot the data
for file_path in file_list:
    # Extract the file name without the extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # Extract the portion of the file name to use as the legend
    legend_label = file_name.split('_')[0]  # Assuming the desired portion is before the first underscore

    # Read the data from the file
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = line.strip().split()  # Assuming columns are space-separated
            data.append((float(x), float(y)))

    # Extract the x and y values from the data
    x_values = [entry[0] for entry in data]
    y_values = [entry[1] for entry in data]

    # Plot the data with the extracted legend label
    plt.plot(x_values, y_values, label=legend_label)

# Add labels and legend
plt.xlabel('Wavelength (nm)')
plt.ylabel('Photoluminescence (a.u.)')
plt.legend()

# Show the plot
plt.show()
