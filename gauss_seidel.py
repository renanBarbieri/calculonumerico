import numpy as np

matrix = np.matrix(
    [10, 2,  3],
    [1,  5,  1],
    [2,  3, 10]
)

# Convergência do Gauss-Seidel:
# -L⁻¹U é < 1 <=> Gauss-Seidel converge

# matriz L
mL = np.matrix(
    [0, 0, 0],
    [1, 0, 0],
    [2, 3, 0],
)

# matriz U
mU = np.matrix(
    [10, 2,  3],
    [0,  5,  1],
    [0,  0, 10]
)

# x = [0.7, -1.6, 0.6]
xKick = [1, 2, 1]
b = [-7,-8,-6]

x[0] = (-(mL[0][1]*xKick[1] + mL[0][2]*xKick[2]) + b[0])/mU[0][0]
x[1] = (-(mL[1][0]*xKick[0] + mL[1][2]*xKick[2]) + b[1])/mU[1][1]
x[2] = (-(mL[2][0]*xKick[0] + mL[2][1]*xKick[1]) + b[2])/mU[2][2]
