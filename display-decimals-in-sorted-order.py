# Find and display decimal numbers in sorted order

from decimal import *
data = list(map(Decimal, '2.45 2.69 2.45 3.45 2.00 0.04 7.25'.split()))
print("Sum: ", sum(data))
print("Sorted order: ", sorted(data))
