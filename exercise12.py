import numpy as np
from numpy.linalg import inv
M = np.array([[3., 1.], [2., 4.]])
inv(M)
print(inv(M))

A = np.array([[7, 5, -3],
              [3, -5, 2], 
              [5, 3, -7]])
r = np.array([[16],
              [-8],
              [0]])
A_inv = inv(A)
np.matmul(A_inv, r)