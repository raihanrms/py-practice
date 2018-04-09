# Create an ASCII waveform

from time import sleep
from math import sin, cos, radians

# increase 40 to get more wave
for n in range(1, 40):
	circle_1 = 50 * (1 + sin(radians(n*10)))
	circle_2 = 50 * (1 + cos(radians(n*10)))
	print("#".center(int(circle_1)))
	print("*".center(int(circle_2)))
	sleep(0.05)
	