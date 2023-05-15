# -*- coding: utf-8 -*-
"""
Created on Mon May 15 17:37:34 2023

@author: T3139
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load the x values from the wavelength file
filename_x = r'E:\tpl\Yiteng\2023\5\power dependent tpl pl npl jordan 08212019\8.48mw\wavelength.txt'
x_data = np.loadtxt(filename_x)
wavelength = x_data[:, 0]

# List of y file names
filenames_y = [
    r'E:\tpl\Yiteng\2023\5\power dependent tpl pl npl jordan 08212019\8.48mw\1250-1450_8.48mw.txt',
    r'E:\tpl\Yiteng\2023\5\power dependent tpl pl npl jordan 08212019\14.9mw\1250-1450_14.9mw.txt',
    r'E:\tpl\Yiteng\2023\5\power dependent tpl pl npl jordan 08212019\23mw\1250-1450_23mw.txt',
    r'E:\tpl\Yiteng\2023\5\power dependent tpl pl npl jordan 08212019\28mw\1250-1450_28mw.txt',
    r'E:\tpl\Yiteng\2023\5\power dependent tpl pl npl jordan 08212019\36mw\1250-1450_36mw.txt'
]

# Function to fit a Gaussian curve
def gaussian(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

# Initialize FWHM list
fwhm_list = []

# Create a figure with a specified size (width, height) in inches and dpi
plt.figure(figsize=(10, 6), dpi=100)

# Iterate over each y file, fit Gaussian curve, and calculate FWHM
for filename_y in filenames_y:
    # Load the y values from the current file
    y_data = np.genfromtxt(filename_y, skip_header=11, skip_footer=1)
    y_data = y_data[:, :]

    # Extract the time and counts arrays
    time = y_data[:, 0]
    counts = y_data[:, 1]

    # Find the indices where the time equals 162.018070
    mask = time == 162.018070
    intensity = counts[mask]

    # Fit a Gaussian curve to the intensity data
    p0 = [np.max(intensity), wavelength[np.argmax(intensity)], 1.0]
    popt, _ = curve_fit(gaussian, wavelength, intensity, p0=p0)

    # Calculate FWHM from the sigma parameter of the Gaussian fit
    fwhm = 2 * np.sqrt(2 * np.log(2)) * popt[2]
    fwhm_list.append(fwhm)

    # Plot wavelength vs. intensity for the current y file
    plt.plot(wavelength, intensity, label=f"FWHM: {fwhm:.3f}")

# Add labels and legend to the plot
plt.xlabel("Wavelength")
plt.ylabel("Intensity")
plt.legend()

# Display the plot
plt.show()

# Print the FWHM values
print("FWHM values:")
for i, fwhm in enumerate(fwhm_list):
    print(f"Curve {i+1}: {fwhm:.3f}")
