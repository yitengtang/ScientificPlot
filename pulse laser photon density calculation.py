# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:17:25 2023

@author: T3139
"""

import math

def calculate_pulse_laser_photon_density(frequency, wavelength, laser_power, beam_size, length, width):
    # Convert wavelength from nm to meters
    wavelength_m = wavelength *1e-9

    # Calculate the pulse energy
    pulse_energy = laser_power / frequency
    print('pulse energy: {:.2e} J'.format(pulse_energy))

    # Calculate the beam area in square meters
    beam_diameter = beam_size*1e6
    beam_area = math.pi * (beam_diameter / 2) ** 2
    print('beam area: {:.2e} nm^2'.format(beam_area))

    # Calculate the number of photons
    plank_constant = 6.62607015e-34  # Planck's constant (J s)
    speed_of_light = 299792458  # Speed of light (m/s)
    num_photons = pulse_energy / ((plank_constant * speed_of_light) / wavelength_m)
    print('photon energy: {:.2e} J'.format((plank_constant * speed_of_light) / wavelength_m))
    print('number of photons: {:.2e}'.format(num_photons))

    # Calculate photon density per square centimeter
    photon_density = num_photons / (beam_area )
    
    #area of the nanoribbons

    area_nanoribbons = length* width #nm^2
    print('area of nanoribbons: {:.2e} nm^2'.format(area_nanoribbons))

    #number of photons accepted by the nanoribbons
    num_photon_per_nanoribbons = photon_density * area_nanoribbons
    print('number of photons accepted by each nanoribbons: {:.2e}'.format(num_photon_per_nanoribbons))

    return photon_density

# Input parameters
frequency = 200e3  # 200 kHz
wavelength = 532  # 532 nm
laser_power = 69e-3  # in W
beam_size = 0.1  # 1.4 mm
nanoribbon_length = 60 #nm
nanoribbon_width = 20 #nm

# Calculate pulse laser photon density
photon_density = calculate_pulse_laser_photon_density(frequency, wavelength, laser_power, beam_size, nanoribbon_length,nanoribbon_width)




# Print the result
print("Pulse laser photon density: {:.2e} photons/nm^2".format(photon_density))
