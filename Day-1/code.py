# with open('input.txt', 'r') as input:
#   result = input.read()
#   print(result)

# import os

# cwd = os.getcwd()  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))

import re

raw_input = open("Day-1/input.txt")
input = (raw_input.read()).split()

# print(input)

listA = sorted(input[::2])
listB = sorted(input[1::2])

# print(listA)
# print(listB)

pairs = zip(listA, listB)
total_distance = 0
similarity_score = 0

for a, b in pairs:
    result = abs(int(b)-int(a))
    # print(f"{a}, {b}")
    total_distance+=result

print(f'Total calculated distance is {total_distance}')

for num in listA:
    result = int(num) * listB.count(num)
    similarity_score+=result

print(f'The Similarity Score is {similarity_score}')