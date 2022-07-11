import sys


def digits_counter(nomber):
    count = 0
    for digit in str(nomber):
        count = count + int(digit)
    return count


args = sys.argv
print(args)
a = int(args[1])

res = digits_counter(a)
print(res)
