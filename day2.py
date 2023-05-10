# Exercises
# Exercise 1
# Create a list of numbers that are less than ten using l_1 and list comprehension


# Your output should [1,5,8,9]

# Use the following list - [1,11,14,5,8,9]

l_1 = [1, 11, 14, 5, 8, 9]

numbers = [l_1 for l_1 in range(1, 11)]


def two_or_more_digits(my_list):
    new_list = []
    for l in my_list:
        if l < 10:
            new_list.append(l)
    return new_list


print(two_or_more_digits(l_1))

# Exercise 2
# Using list comprehension, create a list of names of 4 letters or more and capitalize each name

names1 = ['connor', 'connor', 'bob', 'connor',
          'evan', 'max', 'evan', 'bob', 'kevin']
# Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan',
          'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']

# Is this what you mean by list comprehension 
#  This is what I read to understand, and I added line 37 below. What was I missing
# https://www.programiz.com/python-programming/list-comprehension#:~:text=Points%20to%20Remember-,List%20comprehension%20is%20an%20elegant%20way%20to%20define%20and%20create,and%20loops%20for%20creating%20list.
print([n.capitalize() for n in names1])

names1 = [ n for n in ' ]
print( h_letters)

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
