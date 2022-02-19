# calculate curl of an arbitrary vector against the x,y,z unit vectors

from sympy import *
from sympy.vector import CoordSys3D, curl, matrix_to_vector

# x, y, z = symbols('x y z')
# init_printing(use_unicode=True)

R = CoordSys3D('R')

v1 = R.y*R.i - R.x*R.j + R.z*R.k
curl_v1 = curl(v1)
cM_v1 = Matrix([curl_v1.dot(R.i), curl_v1.dot(R.j), curl_v1.dot(R.k)])

print("v1=", v1)
print("curl(v1) =", curl(v1))
print("curl(v1) matrix=", cM_v1)
print()

v2 = 3*R.y*R.x*R.i + 4*R.x*R.z*R.j -6*R.x*R.k
cM_v2 = Matrix([curl(v2).dot(R.i), curl(v2).dot(R.j), curl(v2).dot(R.k)])

print("v2 = ", v2)
print("curl(v2) = ", curl(v2))
print("curl(v2) matrix = ", cM_v2)
print("curl(v2) matrix_to_vector = ", matrix_to_vector(cM_v2,R))
# print("(",cM_v2.dot(R.i), ",", cM_v2.dot(R.j), ",", cM_v2.dot(R.k), ")")
