# Sleep time
# import time


# def count_down(start, end):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done!")


# print(count_down(1, 5))


# def add(*args):
#     total = 0
#     for x in args:
#         total += x
#     return total


# print(add(1, 2, 3, 4, 5))


# def display_name(*args):
#     for name in args:
#         print(name, end=" ")


# name = display_name("Mr.", "John", "Doe", "Smith")
# print(name)

# Dictionary
# def display_name(**DinaDick):
#     for key, value in DinaDick.items():
#         print(f"{key} :{ value}")

# name = display_name(First="Dina", Last="Dick", Age=33, City="KomPongCham")
# print(name)

def ship_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()


ship_label("Mr.", "Nem", "Sothea", street="Street 1",
           city="Phnom Penh", country="Cambodia")
