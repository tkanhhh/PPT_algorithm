import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    x = np.zeros(n)
    # Forward elimination
    for i in range(n):
        if A[i, i] == 0:
            return "No unique solution exists"
        for j in range(i + 1, n):
            ratio = A[j, i] / A[i, i]
            A[j, :] -= ratio * A[i, :]
            b[j] -= ratio * b[i]
    # Back substitution
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    return x