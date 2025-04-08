# List comprehension = A conscise way to create list in python
#  Compact and easy to read than traditional for loops
# Syntax = [expression for item in iterable]

# Example 1: Create a list of squares from 0 to 9

# traditional for loop
# squares = []
# for x in range(1, 11):
#     squares.append(x*2)
# print(squares)

# squares = [x*2 for x in range(1, 11)]
# print(squares)

# fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)

# Example 2: Create a list of positive numbers
# numbers = [1, -2, 3, -4, 5, -6]
# positive_numbers = [num for num in numbers if num >= 0]
# print(positive_numbers)

# numbers = [1, -2, 3, -4, 5, -6]
# nagavtive_numbers = [num for num in numbers if num <= 0]
# print(nagavtive_numbers)

# numbers = [1, -2, 3, -4, 5, -6, 8, 10, 12, 14, 16, 18]
# event_numbers = [num for num in numbers if num % 2 == 0]
# print(event_numbers)


# numbers = [1, -2, 3, -4, 5, -6, 8]
# odd_numbers = [num for num in numbers if num % 2 == 1]
# print(odd_numbers)

# Example 3 : Create a list
grades = [90, 85, 78, 92, 88]
grade_a = [grade for grade in grades if grade >= 90]
print(grade_a)
