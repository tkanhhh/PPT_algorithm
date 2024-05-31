import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Input Data
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

f = CubicSpline(x, y, bc_type='natural')

# Spline tại x = 2.5
x_to_interpolate = 2.5
spline_value = f(x_to_interpolate)

print(f"Spline tại x = {x_to_interpolate}: {spline_value:.10f}")