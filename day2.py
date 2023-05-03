# Exercises
# Exercise 1
# Create a list of numbers that are less than ten using l_1 and list comprehension


# Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1, 11, 14, 5, 8, 9]

numbers = [l_1 for l_1 in range(1, 11)]


def two_or_more_digits():
    if len(str(num)) < 2:
        numbers.remove(num)
    print(numbers, l_1)


# Exercise 2
# Using list comprehension, create a list of names of 4 letters or more and capitalize each name

names1 = ['connor', 'connor', 'bob', 'connor',
          'evan', 'max', 'evan', 'bob', 'kevin']
# Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan',
          'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

newlist = ['Evan', 'Connor', 'Kevin']
for name in names1:
    if len(name) >= 4:
        print(name.capitalize())

# ['Evan', 'Connor', 'Kevin']
# ['Evan', 'Connor', 'Kevin']
# ['Evan', 'Connor', 'Kevin']
# ['Evan', 'Connor', 'Kevin']
# ['Evan', 'Connor', 'Kevin']
# ['Evan', 'Connor', 'Kevin']
# ['Evan', 'Connor', 'Kevin']
# ['Evan', 'Connor', 'Kevin']
# ['Evan', 'Connor', 'Kevin']
