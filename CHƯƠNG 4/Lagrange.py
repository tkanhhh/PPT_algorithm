import numpy as np
from scipy.interpolate import lagrange

# Input Data
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# Tính đa thức Lagrange
f = lagrange(x, y)

# Lagrange tại x = 2.5
x_to_interpolate = 2.5
spline_value = f(x_to_interpolate)

print(f"Lagrange tại x = {x_to_interpolate}: {spline_value:.10f}")
