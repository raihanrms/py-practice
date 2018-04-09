'''
Ask the user to specify the number of sides on a polygon and find the
number of diagonals within the polygon.
'''

import math
polygons = int (input ("Specify the number of sides of the polygon:"))
n = int(polygons)
diagonals = int( (n*(n-3))/2)
print ("The Polygon of "+str(polygons)+" sides, has " +str(diagonals)+" diagonals")
