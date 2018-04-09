# Sum of all digits of the base to the specified power

def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])


print(power_base_sum(2, 100))
print(power_base_sum(8, 10))
