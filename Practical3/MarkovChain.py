import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt

A = np.array([[1,1,0],[1,0,1],[0,0,1]])

def normalize_conn_matrix(A):
      #converting A to float64 type, then copying that array to T
      T = A.astype(np.float64).copy()
      for i in range(len(A)):
            #dividng every element of a row in T with the sum of the row in A
            T[i] = T[i]/sum(A[i])
      return T

T = normalize_conn_matrix(A)
# print(T)

def appr_stationary(T, maxiter=20):
    """
    T: transition probability,
    maxiter: number of steps
    x_m: the state vector
    """
    x_m = np.repeat(1.0/len(T), len(T))

    for i in range(20):
        x_m = np.matmul(x_m, T)
        
    return x_m

st_dist = appr_stationary(T, maxiter=20)
#print(st_dist)

# print("\n Expected solution:")
# print("[0.00563018 0.00347964 0.99089019]")

def teleporting_factor(T, alpha=0.9):
    """
    T: transition probability,
    alpha: teleporting factor.
    T_new: transition probability after implementing teleporting factor
    """
    T_new = T.copy()
    T_new = alpha * T_new + (1 - alpha) * 1/len(T_new)

    return T_new

def dead_end(A):
    """
    A: connecting matrix
    A_new: connecting matrix by resolving the dead end problem
    """
    A_new = A.copy()
    for i in range(len(A)):
        if (sum(A[i]) == 0):
            A_new[i] = np.repeat(1.0, len(T))
    
    return A_new

teleport = teleporting_factor(T, 0.9)
print("our output:\n")
print(teleport)
print("\n Expected output:")
print("[[0.48333333 0.48333333 0.03333333] \n [0.48333333 0.03333333 0.48333333] \n [0.03333333 0.03333333 0.93333333]]")