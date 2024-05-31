import numpy as np

def least_squares(x, y, degree):
    A = np.vander(x, degree + 1, increasing=True)
    coefficients, _, _, _ = np.linalg.lstsq(A, y, rcond=None)
    return coefficients

# Input Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
degree = 2

coefficients = least_squares(x, y, degree)
print("Hệ số của đa thức bậc", degree, "là:")
print(coefficients)
