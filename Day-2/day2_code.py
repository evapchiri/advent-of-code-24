cleaned_input = [entry.split() for entry in open("./Day-2/input.txt", "r")]
print(cleaned_input[0])


def is_safe_report(report):

  if int(report[0]) > int(report[1]):

    for i in range(len(report) - 1):
      current_num = int(report[i])
      next_num = int(report[i + 1])
      difference = current_num - next_num
      if current_num > next_num and abs(difference) in range(4):
        continue
      else:
        return False

    return True
  
  elif int(report[0]) < int(report[1]):

    for i in range(len(report) - 1):
      current_num = int(report[i])
      next_num = int(report[i + 1])
      difference = current_num - next_num
      if current_num < next_num and abs(difference) in range(4):
        continue
      else:
        return False
      
    return True
  
  else: 
    return False


count = 0
for report in cleaned_input:
  if is_safe_report(report):
    count +=1

print(f'\n>>>> We have {count} safe reports! <<<<\n')