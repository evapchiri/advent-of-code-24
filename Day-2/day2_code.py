cleaned_input = [entry.split() for entry in open("./Day-2/input.txt", "r")]
# print(cleaned_input[0])


def is_safe_report(report):
## 1 2 7 8 9
  is_increasing = int(report[0]) < int(report[1])
  for i in range(len(report) - 1):
    current_num = int(report[i])
    next_num = int(report[i + 1])
    difference = abs(current_num - next_num)

    if is_increasing and current_num < next_num and difference in range(4):
        continue
    if (not is_increasing) and current_num > next_num and difference in range(4):
        continue
    return False
  return True
  


count = 0
for report in cleaned_input:
  if is_safe_report(report):
    count +=1

print(f'\n>>>> We have {count} safe reports! <<<<\n')


def is_safe_with_dampener(report):
  possibilities = [report[:i] + report[i+1:] for i in range(len(report))]
  case_checks = []
  for case in possibilities:
    if is_safe_report(case):
      return True
    
  return False
    

# print(case_checks.count(False))
# print(case_checks)

# print(cleaned_input[1])
# print(is_safe_with_dampener(cleaned_input[1]))

final_count = 0
for report in cleaned_input:
  if is_safe_with_dampener(report):
    final_count +=1

print(f'\n>>>> We have {final_count} safe reports! <<<<\n')