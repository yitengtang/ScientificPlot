# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:45:00 2023

@author: T3139
"""

import numpy as np
import matplotlib.pyplot as plt

# Load the x values from the first file
filename1 = r'E:\tpl\Yiteng\2023\4\npl ase lense focaus\11mw\test\wavelength.txt'
x_data = np.loadtxt(filename1)
wavelength = x_data[:,0]

# Load the y values from the second file
filename2 = r'E:\tpl\Yiteng\2023\4\npl ase lense focaus\11mw\test\TIMETAG-DATA11.txt'
y_data = np.genfromtxt(filename2, skip_header= 11,skip_footer=1)
# Delete the last row of the y_data array
y_data = y_data[:, :]


# Extract the time and counts arrays
time = y_data[:,0]
counts = y_data[:,1]

# Find the indices where the time equals 162.018070 we can use multiple mask to extract more data to plot
mask = time == 162.018070
intensity = counts[mask]

# Plot wavelength vs. intensity
plt.plot(wavelength, intensity)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.show()
