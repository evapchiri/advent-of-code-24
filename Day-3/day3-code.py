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

# print(new_input)

def mul(a,b):
  return a * b

total = 0

for operation in new_input:
  total += eval(operation.strip("'"))
  # result = eval(operation.strip("'"))
  # print(type(result))

print(f'> > INITIAL TOTAL IS {total}')
# print(new_input[0].strip("'"))


""""""""""""

# def finding(string, char):
#     return [i for i, character in enumerate(string) if character == char]

# list_indexes = finding(input, "don't()")

# print(list_indexes)



split = input.split("don't()")
print(split[0])

to_keep = []

for cut in split:
  i = 0
  # print(f'>>>>>>>>>>>>>> ANALYSING {cut}')
  if i == 0:
    to_keep.append(cut)
    i += 1
    continue
  elif "do()" in cut:
    # print(f'WE HAVE KEPT {cut}!! ⭐️\n\n')
    to_keep.append(cut)
    i += 1
  else:
    # print(f'WE HAVE NOT KEPT {cut} 😔\n\n')
    i += 1
    continue

# new_string = [input[cut.find('do()'):] for cut in input if "do()" in cut]


# print(input.find('do()'))

cleaned_input = to_keep[0]
for str in to_keep[1:]:
  cleaned_input = cleaned_input + str[str.find('do()'):]

# print(cleaned_input)

total_from_enabled_ops = 0

final_input = re.findall("mul\(\d{1,3},\d{1,3}\)", cleaned_input)

for operation in final_input:
  total_from_enabled_ops += eval(operation.strip("'"))

print(f' ⭐️ -> -> FINAL TOTAL IS {total_from_enabled_ops} <- <- ⭐️')