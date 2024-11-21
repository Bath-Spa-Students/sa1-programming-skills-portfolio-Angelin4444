#Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console in each case.
"""
Write a loop that counts up from 0 to 50 in increments of 1.
Write a loop that counts down from 50 to 0 in decrements of 1.
Write a loop that counts up from 30 to 50 in increments of 1.
Write a loop that counts down from 50 to 10 in decrements of 2.
Write a loop that counts up from 100 to 200 in increments of 5. You may include all loops in a single project
"""

# Counting in ascending order(0 to 50), one number at a time(+1).
print("Counting up from 0 to 50 by adding 1 each time:")
for a in range(0, 51, 1):
    print(a)

# Counting in descending order(50 to 0), one number at a time(-1).
print("\nCounting down from 50 to 0 by subtracting 1 each time:")
for b in range(50, -1, -1):
    print(b)

# Counting in ascending order(30 to 50), one number at a time(+1)
print("\nCounting up from 30 to 50 by adding 1 each time:")
for c in range(30, 51, 1):
    print(c)

# Counting descending order(50 to 10),adding 2 numbers
print("\nCounting down from 50 to 10 by subtracting 2 each time:")
for d in range(50, 9, -2):
    print(d)

# Counting ascending order(100 to 200), adding 5 numbers
print("\nCounting up from 100 to 200 by adding 5 each time:")
for e in range(100, 201, 5):
    print(e)
