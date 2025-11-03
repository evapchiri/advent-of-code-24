import re
import string

input = open('./Day-3/input.txt', 'r').read()
# print(input)
# print(re.replace(string.punctuation))

# print(string.punctuation)

# spec_char = [char for char in string.punctuation]
# print(spec_char)

# re.replace(input,)
# new_input = ''
# for char in spec_char:
#   new_input = re.sub(char, " ", input)

new_input = re.findall("mul\(\d{1,3},\d{1,3}\)", input)

# print(f'>>>>>>>>>> PREVIOUS INPUT: {input}')

print(new_input)
