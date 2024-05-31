import numpy as np
from scipy.linalg import lu, lu_solve, lu_factor

def lu_factorization(A, b):
    P, L, U = lu(A)
    
    lu_and_piv = lu_factor(A)
    x = lu_solve(lu_and_piv, b)
    
    return L, U, x

# input data
A = np.array([[7, 3, -1, 2], 
              [3, 8, 1, -4], 
              [-1, 1, 4, -1], 
              [2, -4, -1, 6]])

b = np.array([1, 4, 2, 3])

L, U, x = lu_factorization(A, b)

print("Ma trận L:")
print(L)

print("Ma trận U:")
print(U)

print("Nghiệm của hệ phương trình là:")
print(x)
