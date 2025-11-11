# create a dict of main values : {'behind': [list of values that need to be behind], 'infront': [list of values that need to be infront]}
# for each line check that -> value being investigated (X) have both ^ cases True. i.e.:
#   if all values behind X are in X['behind'] AND that all values in front of X are in x['infront] -> then we gucci 
# and 'correctly_ordered' remains TRUE // otherwise 'correctly_ordered' is FALSE so byebye 👋

input = open('./Day-5/input.txt', 'r').read()

sectioned_input = input.split('\n\n')

ordering_rules = sectioned_input[0].split('\n')
updates_to_print = sectioned_input[1].split('\n')

###  creating the ORDERING dict ....

def get_order_rules_infront_of(ordering_rules:list): # format like ['92|21', '13|9',...]
  """
  From a list of ordering rules with format '92|23' gives back a dict where page KEY must be printed BEFORE the pages VALUES.
  """
  rules_dict = {}
  for rule in ordering_rules:
    values = [int(value) for value in rule.split('|')]
    if values[0] not in rules_dict.keys():
      rules_dict[values[0]] = [values[1]]
    else:
      rules_dict[values[0]].append(values[1])
    
  return rules_dict

def get_order_rules_behind_of(ordering_rules:list): # format like ['92|21', '13|9',...]
  """
  From a list of ordering rules with format '92|23' gives back a dict where page KEY must be printed AFTER the pages VALUES.
  """
  rules_dict = {}
  for rule in ordering_rules:
    values = [int(value) for value in rule.split('|')]
    if values[1] not in rules_dict.keys():
      rules_dict[values[1]] = [values[0]]
    else:
      rules_dict[values[1]].append(values[0])

  return rules_dict

def page_in_correct_order(allowed_values, page, next_pages, prev_pages):
        first_check = all(value in allowed_values[page]['print_before'] for value in next_pages)
        second_check = all(value in allowed_values[page]['print_after'] for value in prev_pages)
        if first_check and second_check:
          return True
        else:
          return False

def get_correct_ord_updates(allowed_values:dict, updates_to_print:list):
  """
  Gives back a LIST of correctly ordered updates. Each update is now a LIST of int (pages).
  """
  correctly_ordered = []
  for update in updates_to_print:

    is_updt_correctly_ordered = True
    list_pages = [int(page) for page in update.split(',')]
    i = 0
    for page in list_pages:
      prev_pages = list_pages[:i]
      next_pages = list_pages[i+1:]
      i += 1
      if not (page_in_correct_order(allowed_values,page,next_pages,prev_pages)):
        is_updt_correctly_ordered = False
        continue
    if is_updt_correctly_ordered:
      correctly_ordered.append(list_pages)
    else:
      next
  return correctly_ordered

def get_incorrect_ord_updates(allowed_values:dict, updates_to_print:list):
  """
  Gives back a LIST of incorrectly ordered updates. Each update is now a LIST of int (pages).
  """
  incorrectly_ordered = []
  for update in updates_to_print:

    list_pages = [int(page) for page in update.split(',')]
    i = 0
    # print(f'>>>>>>>>> CHECKING NOW {list_pages}')
    for page in list_pages:
      # print(f'>>>>> THE PAGE IS: {page} from LIST: {list_pages}')
      prev_pages = list_pages[:i]
      # print(f' Previous pp are: {prev_pages}')
      next_pages = list_pages[i+1:]
      # print(f' Next pp are: {next_pages}\n')
      i += 1
      # print(f'🔍 CHECKING {page}\nFIRST CHECK IS: {first_check} & SECOND CHECK IS {second_check}')
      if not (page_in_correct_order(allowed_values,page,next_pages,prev_pages)):
        # print(f'    ❌ {page} BROKE THE RULES ORDERED')
        # print(f'First check was {first_check} and second check was {second_check}')
        incorrectly_ordered.append(list_pages)
        # print(f'⭐️ INCORRECTLY ORDERED IS NOW:\n {correctly_ordered}')
        break
  return incorrectly_ordered

def make_correct(page:int, page_index:int, incorrect_update:list, allowed_values:dict):
    
  set_rules = {}
  for page in incorrect_update:
    set_rules[page] = set(incorrect_update).intersection(set(allowed_values[page]['print_before']))

  #sanitising the set_rules dict - removing key: set() from ^
  for key,value in set_rules.items():
    if value == set():
      set_rules[key] = {}
  
  corrected_update = sorted(set_rules, key=lambda key: len(set_rules[key]))

  return corrected_update


def correct_incorrect_updates(allowed_values:dict, updates_to_correct:list):
  """
  As it finds an incorrect update, it will correct it. Gives back the list of previously incorrect updates, now corrected.
  """
  corrected_updates = []
  for update in updates_to_correct:
    i = 0
    for page in update:
      prev_pages = update[:i]
      next_pages = update[i+1:]
      if not (page_in_correct_order(allowed_values,page,next_pages,prev_pages)):
        corrected_updates.append(make_correct(page, i, update, allowed_values))
        break
      i += 1
  return corrected_updates

def count_mid_values(list_of_updates:list): #of integers

  count = 0

  for update in list_of_updates:
    count += update[len(update)//2]

  return count

pages_to_be_printed_AFTER = get_order_rules_infront_of(ordering_rules)
pages_to_be_printed_BEFORE = get_order_rules_behind_of(ordering_rules)

allowed_values = {} 
  # This ^ will look like:
  # KEY IS : 2 and has: {'print_before': [1], 'print_after': []}
  # KEY IS : 3 and has: {'print_before': [1], 'print_after': [8, 4]}
  # KEY IS : 4 and has: {'print_before': [1, 3], 'print_after': [8]}
  # KEY IS : 8 and has: {'print_before': [4, 3], 'print_after': []}
  # KEY IS : 1 and has: {'print_before': [], 'infront': [2, 3, 4]}

for key, value in pages_to_be_printed_AFTER.items():
  if key in pages_to_be_printed_BEFORE.keys():
    allowed_values[key] = {'print_before': pages_to_be_printed_AFTER[key], 'print_after': pages_to_be_printed_BEFORE[key]}
  else:
    allowed_values[key] = {'print_before': pages_to_be_printed_AFTER[key], 'print_after': []}

for key, value in pages_to_be_printed_BEFORE.items():
  if key in allowed_values.keys():
    continue # as it was done in step before
  else:
    allowed_values[key] = {'print_before': [], 'print_after': pages_to_be_printed_BEFORE[key]}


correct_updates = get_correct_ord_updates(allowed_values, updates_to_print)
incorrect_updates = get_incorrect_ord_updates(allowed_values,updates_to_print)
CORRECTED_updates = correct_incorrect_updates(allowed_values,incorrect_updates)

print(f'\nFULL LIST OF UPDATES IS {len(updates_to_print)} LONG\n')

print(f'\nFROM {len(correct_updates)} CORRECT UPDATES ---> THE SUM OF MIDDLE VALUES IS ⭐️ {count_mid_values(correct_updates)} ⭐️\n')

print(f'\nFROM {len(incorrect_updates)} INCORRECT UPDATES ---> AFTER CORRECTING THEM, THE SUM OF MIDDLE VALUES IS ⭐️ {count_mid_values(CORRECTED_updates)} ⭐️\n')

