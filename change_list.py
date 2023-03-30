a = [1, 2, 3, 4, 5]
print(a[1])
a[1] = 33  # changes 2 to 33
print(a)

# s = "Cat"
# s[0] = "R"
# print(s)  # does not work because it is a string and strings are unmutable

a = [1, 2, 3, 4, 5]
b = a
a[1] = 33
b[1] = 44
print(a, b)

a = [1, 2, 3]
b = [1, 2, 3]
a[1] = 22
b[2] = 44
print(a, b)