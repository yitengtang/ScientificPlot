# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:45:00 2023

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
y_data = np.genfromtxt(filename2, skip_header= 0,skip_footer=0)
# Delete the last row of the y_data array
y_data = y_data[:, :]


# Extract the time and counts arrays
time = y_data[:,0]
counts = y_data[:,1]

# Find the indices where the time equals 162.018070 we can use multiple mask to extract more data to plot
mask = time == 162.018070
intensity = counts[mask]
mask1 = time == 166.927708
intensity1 = counts[mask]
mask2 = time == 171.837347
intensity2 = counts[mask]
mask3 = time == 176.746985
intensity3 = counts[mask]

# Plot wavelength vs. intensity
plt.plot(wavelength, intensity)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.show()

plt.plot(wavelength, intensity1)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.show()
plt.plot(wavelength, intensity2)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.show()