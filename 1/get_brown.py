import numpy as np
import matplotlib.pyplot as plt

def get_brownian_motion(steps, number_of_particles):
    motions = np.random.randn(steps,number_of_particles)
    motions[0] = np.zeros(number_of_particles)
    return motions