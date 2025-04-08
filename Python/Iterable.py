# Iterable = An object/collection the can return its elements one at a time

# numbers = (1, 2, 3, 4, 5)

# for number in reversed(numbers):
#     print(number, end=" ")

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number, end=" ")

# Set
# fruits = {"apple", "banana", "cherry"}

# for fruit in fruits:
#     print(fruit, end=" ")

my_dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")
# Output: name: John age: 30 city: New York
