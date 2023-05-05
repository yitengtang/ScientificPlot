# -*- coding: utf-8 -*-
"""
Created on Fri May  5 14:50:00 2023

@author: T3139
"""

import numpy as np
import matplotlib.pyplot as plt

# Load the x values from the first file
filename1 = r'C:\Users\T3139\wavelength1.txt'
x_data = np.loadtxt(filename1)
wavelength = x_data[:,0]

# Load the y values from the second file
filename2 = r'C:\Users\T3139\tpl data.txt'
y_data = np.genfromtxt(filename2, skip_header= 0, skip_footer=0)
# Delete the last row of the y_data array
y_data = y_data[:, :]

# Extract the time and counts arrays
time = y_data[:,0]
counts = y_data[:,1]

# Find the indices where the time equals 162.018070, 166.927708, 171.837347, 176.746985
mask1 = time == 162.018070
mask2 = time == 166.927708
mask3 = time == 171.837347
mask4 = time == 176.746985

# Extract the intensity values corresponding to each time value
intensity1 = counts[mask1]
intensity2 = counts[mask2]
intensity3 = counts[mask3]
intensity4 = counts[mask4]

# Plot all the intensity values in a single graph
plt.plot(wavelength, intensity1, label='162.018070')
plt.plot(wavelength, intensity2, label='166.927708')
plt.plot(wavelength, intensity3, label='171.837347')
plt.plot(wavelength, intensity4, label='176.746985')

# Set the x and y labels
plt.xlabel("Wavelength")
plt.ylabel("Intensity")

# Set the legend
plt.legend()

# Show the plot
plt.show()
