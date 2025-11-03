cleaned_input = [entry.split() for entry in open("./Day-2/input.txt", "r")]
# print(cleaned_input[0])


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


# def prob_dampener(report, change_allowance):
#   change_allowance = change_allowance
  
#   if int(report[0]) > int(report[1]):
#     for i in range(len(report) - 1):
#       current_num = int(report[i])
#       next_num = int(report[i + 1])
#       difference = current_num - next_num
#       if current_num > next_num and abs(difference) in range(4):
#         continue
#       else:
#         if change_allowance is not 0 and i == 0:
#             print(f'RECURSIVE report WAS {report}')
#             report.pop(0)
#             print(f'RECURSIVE report NOW is {report}')
#             return prob_dampener(report, 0)
#         elif change_allowance > 0 and abs(int(report[i - 1]) - next_num) in range(1,4):
#           change_allowance -= 1
#           continue
#         else:
#           # print(f'report {report} has been tagged as FALSE')
#           return False
#     return True
  
#   elif int(report[0]) < int(report[1]):
#     for i in range(len(report) - 1):
#       current_num = int(report[i])
#       next_num = int(report[i + 1])
#       difference = current_num - next_num
#       if current_num < next_num and abs(difference) in range(4):
#         continue
#       else:
#         if change_allowance is not 0 and i == 0:
#             print(f'RECURSIVE report WAS {report}')
#             report.pop(0)
#             print(f'RECURSIVE report NOW is {report}')
#             return prob_dampener(report, 0)
#         elif change_allowance > 0 and abs(int(report[i - 1]) - next_num) in range(1,4):
#           change_allowance -= 1
#           continue
#         else:
#           # print(f'report {report} has been tagged as FALSE')
#           return False
#     return True
  
#   else: 
#     return False


# def prob_dampener2(report):
#   popping = len(report)
#   is_safe = []
#   for i in range(popping - 1):
#     report.pop(i)
#     if int(report[0]) > int(report[1]):
#       for i in range(len(report) - 1):
#         current_num = int(report[i])
#         next_num = int(report[i + 1])
#         difference = current_num - next_num
#         if current_num > next_num and abs(difference) in range(4):
#           continue
#         else:
#           is_safe.append(False)

#       is_safe.append(True)
    
#     elif int(report[0]) < int(report[1]):

#       for i in range(popping - 1):
#         current_num = int(report[i])
#         next_num = int(report[i + 1])
#         difference = current_num - next_num
#         if current_num < next_num and abs(difference) in range(4):
#           continue
#         else:
#           is_safe.append(False)
        
#       is_safe.append(True)
    
#     else: 
#       is_safe.append(False)
  
#   if False in is_safe:
#     return False
  
#   else:
#     return True



# new_count = 0
# for report in cleaned_input:
#   if prob_dampener2(report):
#     new_count +=1

# print(f'\n>>>> DAMPENER: We have THEN {new_count} safe reports! <<<<\n')

# test_input = ['7 6 4 2 1','1 2 7 8 9','9 7 6 2 1','1 3 2 4 5','8 6 4 4 1','1 3 6 7 9', '1 9 8 7 6 5', '40 35 32 31 28 25']
# if prob_dampener(test_input[7].split(),1):
#   print('TEST WAS TRUE!')
