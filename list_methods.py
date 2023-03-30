list_methods = dir([])
for method in list_methods:
    if method.startswith("__"):
        continue
    print(method)

a = [1, 2, 3]
a.append(7)  # writes whatever you want at the end of the list
a.append("james")
print(a)
# a.clear()  # returns empty list
# print(a)
b = a.copy()
a = [1, 1, 1, 1, 2, 2, 2, 1, 1]
print(a.count(1))  # how many times that item appears
a = ["bob", "james", "jane"]
print(a.index("jane"))  # tells in which position is that item
e = a.pop()  # takes one item out of the list. If I don't specify which one it pops the last one
print(e, a)

import random
a = []
for i in range(100):
    a.append(random.randint(1, 1000))  # append adds an element to the list
print(a)
a.sort(reverse=True)
print(a)

# I have to say pop[1], but remove["james"]