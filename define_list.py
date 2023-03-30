a = []
print(f"a is {a}, type of a={type(a)}")

a = [1, 2, 3, 4]
print(a)
b = [3.3, -9, 0, 11, "bob"]
print(b)
c = [1, 1.2, 0, True, "xxxx", print, None]  # all are valid items to put into a list
print(c)
print(b[1])
c[5](b[1])  # unnecessarily complex
# print(c[11])  # error, there is no such item in the list
print(c[-1])  # backwards
print(len(c))  # number of elements in the list
d = a + b
print(d)  # concatenates both lists
d = 3*a
print(a)  # one list with three times the list a. Here the length is 12
d = [a, a, a, a]  # here the length is 4
print(d)
print(d, d[2][2])  # index 2, position 2, that's why it print "3"
