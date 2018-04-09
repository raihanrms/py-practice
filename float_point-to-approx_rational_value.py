# Convert a floating point number to an approximate rational value

import fractions
import math

print('PI       =', math.pi)

f_pi = fractions.Fraction(str(math.pi))
print('No limit =', f_pi)

for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = f_pi.limit_denominator(d)
    print('{0:8} = {1}'.format(d, limited))
