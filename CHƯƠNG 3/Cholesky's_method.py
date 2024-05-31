import numpy as np
import scipy.linalg as sla

# example matrix A
A = np.array([
        [9, -3, -3],
        [-3, 10, 1],
        [3, 1, 5]])
# Cholesky
L = np.linalg.cholesky(A)
print("Ma trận L:")
print(L)