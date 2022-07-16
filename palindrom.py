import sys
import re

def is_palindrome(text):
    text = text.lower()
    text = re.sub(r'[\W_]+', '', text)
    print (text)
    rev = text[::-1]
    res = text == rev
    return res

test = is_palindrome(sys.argv[1])
print (test)