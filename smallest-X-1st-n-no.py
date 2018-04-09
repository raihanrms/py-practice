# Finding the smallest multiple of the first n numbers

def smallest_multiple(n):
    i = n * 2
    factors = [number  for number in range(n, 1, -1) if number * 2 > n]
    print(factors)

    while True:
        for a in factors:
            if i % a != 0:
                i += n
                break
            if (a == factors[-1] and i % a == 0):
                return i
                
print(smallest_multiple(13))
print(smallest_multiple(11))
