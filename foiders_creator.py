import os

i = 0
limit = 300

while i < limit:
    os.mkdir("tmp/" + str(i))
    i = i + 1
