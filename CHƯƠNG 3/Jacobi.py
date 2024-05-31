import numpy as np

def jacobi(A, b, x0, tol=1e-6, maxiter=200):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = x0.copy()
    for i in range(maxiter):
        x_new = (b - np.dot(R, x)) / D
        if np.linalg.norm(x_new - x) < tol:
            return x_new
        x = x_new
    return x