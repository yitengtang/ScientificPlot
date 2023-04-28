# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 17:45:00 2023

@author: T3139
"""

import numpy as np
import matplotlib.pyplot as plt

# Load the x values from the first file
x_data = np.loadtxt("wavelength1.txt")
wavelength = x_data[:,0]

# Load the y values from the second file
y_data = np.loadtxt("tpl data.txt")
time = y_data[:,0]
counts = y_data[:,1]

# Find the indices where the time equals 162.018070
mask = time == 162.018070
intensity = counts[mask]

# Plot wavelength vs. intensity
plt.plot(wavelength, intensity)
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.show()
