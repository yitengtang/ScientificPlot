# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 16:31:13 2023

@author: T3139
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# define Gaussian function
def gaussian(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2*sigma**2))

# load data from file
filename = r'E:\PL\2023\4\jordan npl_pmt_nd1.txt - adjusted.txt'
data = np.loadtxt(filename)

# extract columns
wavelength = data[:,0]
intensity = data[:,1]

# fit Gaussian function multiple times and choose best fit
num_fits = 100
best_fit = None
best_residuals = None
best_ss_res = float('inf')
for i in range(num_fits):
    # initial guess for parameters
    p0 = [max(intensity), np.mean(wavelength), np.std(wavelength)]
    # add noise to the data
    noisy_intensity = intensity + np.random.normal(0, 0.01, len(intensity))
    # perform curve fitting
    popt, pcov = curve_fit(gaussian, wavelength, noisy_intensity, p0=p0)
    # calculate sum of squared residuals
    y_fit = gaussian(wavelength, *popt)
    residuals = noisy_intensity - y_fit
    ss_res = np.sum(residuals**2)
    # update best fit if necessary
    if ss_res < best_ss_res:
        best_fit = popt
        best_residuals = residuals
        best_ss_res = ss_res

# calculate R-squared value for best fit
y_fit = gaussian(wavelength, *best_fit)
ss_tot = np.sum((intensity - np.mean(intensity))**2)
r_squared = 1 - (best_ss_res / ss_tot)

# create plot
fig, ax = plt.subplots()

# plot data
ax.plot(wavelength, intensity, 'b-', label='data')

# plot Gaussian fit
x_fit = np.linspace(wavelength.min(), wavelength.max(), 1000)
y_fit = gaussian(x_fit, *best_fit)
ax.plot(x_fit, y_fit, 'r-', label='fit')

# plot residuals
ax.plot(wavelength, best_residuals, 'g-', label='residuals')

# set plot properties
ax.set_xlabel('Wavelength (nm)')
ax.set_ylabel('Intensity (arb. units)')
ax.set_title('Photoluminescence Measurement with Gaussian Fit\nR-squared = {:.3f}'.format(r_squared))
ax.legend()

# add R-squared value to plot
textstr = 'R-squared = {:.3f}'.format(r_squared)
props = dict(boxstyle='round', facecolor='white', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)

# show the plot
plt.show()


