# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = list(range(10))  # the same but easier
# print(a, b)

b = list(range(20))
print(b)

print(b[::2])  # slice list with even numbers
b = list(range(0, 20, 2))  # same thing but with generate
print(b)
print(b[-2::-2])
a = list(range(20))
print(a, a[5:])