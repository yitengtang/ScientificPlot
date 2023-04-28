# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 14:53:25 2023

@author: T3139
"""

import numpy as np
from scipy.optimize import curve_fit
import plotly.graph_objs as go

# define Gaussian function
def gaussian(x, A, mu, sigma):
    return A*np.exp(-(x-mu)**2/(2*sigma**2))

# load data from file
filename = r'E:\PL\2023\4\jordan npl_pmt_nd1.txt - adjusted.txt'
data = np.loadtxt(filename)

# extract columns
wavelength = data[:,0]
intensity = data[:,1]

# perform curve fitting
p0 = [max(intensity), np.mean(wavelength), np.std(wavelength)]
popt, pcov = curve_fit(gaussian, wavelength, intensity, p0=p0)

# create trace for data
trace_data = go.Scatter(x=wavelength, y=intensity, name='data')

# create trace for Gaussian fit
x_fit = np.linspace(wavelength.min(), wavelength.max(), 1000)
y_fit = gaussian(x_fit, *popt)
trace_fit = go.Scatter(x=x_fit, y=y_fit, name='fit')

# create layout for plot
layout = go.Layout(title='Photoluminescence Measurement with Gaussian Fit',
                   xaxis=dict(title='Wavelength (nm)'),
                   yaxis=dict(title='Intensity (arb. units)'))

# combine traces and layout and create figure
fig = go.Figure(data=[trace_data, trace_fit], layout=layout)

# show the figure
fig.show(renderer='browser')

