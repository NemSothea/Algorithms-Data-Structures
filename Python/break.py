# Break and continue Statements
# for n in range(2,10):
#     for x in range(2,n):
#         if n % x == 0:
#             print(f"{n} equals {x} * {n//x}")
#             break

# for num in range(2, 10):
#     if num % 2 == 0:
#         print(f"Found an even number {num}")
#         continue
#     print(f"Found a number {num}")
def find(num):
    for i in range(1, num):
        if i % 2 == 0:
            print(f"{i}")


find(10)
