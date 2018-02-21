from numpy import *
def pinv(A):
    A = linalg.inv(A.T * A) * A.T
    return A