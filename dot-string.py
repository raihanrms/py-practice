# Create a dot string

from math import sin, cos, radians
import sys
for i in range(1000):
    print(' '*int(10*cos(radians(i))+10) + '.')
	