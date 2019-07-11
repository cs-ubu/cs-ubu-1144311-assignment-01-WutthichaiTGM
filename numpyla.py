import numpy as np
import numpy.linalg as linalg

A = np.array( 
    [
        [ 4.0, -2.0,  1.0],
        [-2.0,  4.0, -2.0],
        [ 1.0, -2.0,  3.0] 
    ] 
)
b = np.array([1.0,4.0,2.0])
# 4.0*1.0+-2.0*4.0+1.0*2.0

A[0][0]*b[0] + A[0][1]*b[1] + A[0][2]*b[2]
A[1][0]*b[1] + A[1][1]*b[1] + A[1][2]*b[2]
A[2][0]*b[2] + A[2][1]*b[1] + A[2][2]*b[2]

print(np.dot(A,b))