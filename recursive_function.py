def factorial(num):
    product = 1
    for i in range(2, num+1):
        product *= i
    return product

def rec_fac(num):
    if num == 1:
        return 1  # escape mechanism
    return num*rec_fac(num-1)

print(rec_fac(5))