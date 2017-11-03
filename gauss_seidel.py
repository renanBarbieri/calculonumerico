import numpy as np

matrix = np.matrix([
    [10,2,3],
    [1,5,1],
    [2,3,10]
])

print(matrix)

# Convergência do Gauss-Seidel:
# -L⁻¹U é < 1 <=> Gauss-Seidel converge

# matriz L
mL = np.matrix('0 0 0; 1 0 0; 2 3 0')
print("mL: %s" %(mL))

# matriz U
mU = np.matrix('10 2 3; 0 5 1; 0 0 10')
print("mU: %s" %(mU))

# x = [0.7, -1.6, 0.6]
xKick = [1, 2, 1]
print("xKick: %s" %(xKick))

b = [-7,-8,-6]

xKick[0] = (-(mL.item(0,1)*xKick[1] + mL.item(0,2)*xKick[2]) + b[0])/mU.item(0,0)
xKick[1] = (-(mL.item(1,0)*xKick[0] + mL.item(1,2)*xKick[2]) + b[1])/mU.item(1,1)
xKick[2] = (-(mL.item(2,0)*xKick[0] + mL.item(2,1)*xKick[1]) + b[2])/mU.item(2,2)

print("xKick: %s" %(xKick))