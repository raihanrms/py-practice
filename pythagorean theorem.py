'''

Take the lengths of two sides to a triangle from the user and apply the 
Pythagorean Theorem to find the third

'''

import math
print ("Enter Side A and B of the triangle to get side C.") 
side_A = int (input ("Enter Side A:")) 
side_B = int (input ("Enter Side B:")) 
a = side_A 
b = side_B 
side_C = math.sqrt ((a ** 2 + b ** 2)) 
c = side_C 
print ("Side C is:" + str (c)) 
print ("Side C is:" + str (round (c, 2)))
