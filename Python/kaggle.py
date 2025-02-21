# Document: https://www.kaggle.com/code/colinmorris/functions-and-getting-help
# Day 01
# spam_amount = 0
# print(spam_amount)

# # Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
# spam_amount = spam_amount + 4

# if spam_amount > 0:
#     print("But I don't want ANY spam!")

# viking_song = "Spam " * spam_amount
# print(viking_song)


# def least_defference(a, b, c):
#     differences = min(abs(a - b), abs(b - c), abs(a - c))
#     return differences


# print(
#     least_defference(1, 5, 9),
#       least_defference(1, 10, 10)
#       )

def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)
def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))
print(call(mult_by_five,1),
      squared_call(mult_by_five, 1)
      )


