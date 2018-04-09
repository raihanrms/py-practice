'''
Making a multiplication table
'''

table = 8
start = 1
max = 10
print "-" * 20
print "The table of 8"
print "-" * 20
i = start
while i <= max:
    result = i * table
    print i, " * ", table, " =" , result
    i = i + 1
print "-" * 20
print "Done counting...."
print "-" * 20
