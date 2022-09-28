#program to find angle between two vectors

import math

vector1  = [6,8]
vector2 = [0,-8]

dot_product = (vector1[0]*vector2[0]+vector1[1]*vector2[1])/(math.sqrt(vector1[0]**2+vector1[1]**2)*math.sqrt(vector2[0]**2+vector2[1]**2))
print("the dot product is " + str(dot_product))
angle = math.acos(dot_product)
print("the angle is " + str(angle))