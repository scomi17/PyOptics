from math import *


# find the refractive index of a rotational translation stage used with michelson interferometer
def refractive_index(thickness, fringes, wavelength, angle):
    numerator = ((2 * thickness) - (fringes * wavelength)) * (1 - cos((angle * pi) / 180))
    denominator = (2 * thickness) * (1 - cos((angle * pi) / 180)) - (fringes * wavelength)
    return numerator / denominator


# finds the angle relating to the fringe shift
def angle_fringe_shift(thickness, wavelength, refractive_index, fringes):
    numerator = (fringes * wavelength * refractive_index)
    denominator = (2 * refractive_index * thickness) - (2 * thickness - fringes * wavelength)
    return 1 - (numerator / denominator)


# finds the path difference of two waves
def path_difference(thickness, refractive_index, angle):
    numerator = thickness
    denominator = sqrt(1 - pow((sin(angle) / refractive_index), 2))
    return 2 * (numerator / denominator - thickness)


# finds the phase difference of two waves
def phaseDifference(path_difference, wavelength):
    return (2*pi*path_difference)/wavelength


# finds the interference intensity caused by two waves
def interferenceIntensity(PHD, intensity1, intensity2):
    return intensity1 + intensity2 + 2*sqrt(intensity1*intensity2)*cos(PHD)

