'''
Example 1

Let's say you want to find out how much you weigh in stone.
Since a stone is 14 pounds, and there are about 2.2 pounds 
in a kilogram

Solution
'''

mass_kg = int(input("What is your mass in kilogram? = " ))
mass_stone = mass_kg * 2.2 / 14
print("You weigh", mass_stone, "in stones.")
