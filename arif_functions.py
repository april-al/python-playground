import sys


def add(a, b):
    res = a + b
    print(res)
    return res


def devision(a, b):
    if b == 0:
        print('illegal argument')
        return
    res = a / b
    print(res)
    return res


def powpow(a, b):
    res = a ** b
    print(res)
    return res


def multiply(a, b):
    res = a * b
    print(res)
    return res


def reminder(a, b):
    res = a % b
    print(res)
    return res


args = sys.argv
print(args)
a = int(args[1])
b = int(args[2])

add(a, b)
devision(a, b)
powpow(a, b)
multiply(a, b)
reminder(a, b)
