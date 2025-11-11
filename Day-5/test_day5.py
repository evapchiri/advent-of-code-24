import unittest
import day5_code

# class TestDay5Code(unittest.TestCase):

#   def test_(self):
#     self.assertEqual()


test_ordering_rules = ['2|1', '3|1', '4|1', '8|4', '8|3', '4|3', '3|2', '4|2']

test_updates_to_print = ['4, 3, 2, 1', '1,3,4,8', '8,4,3']

# order_rules_behind = day5_code.get_order_rules_infront_of(test_ordering_rules)
# order_rules_infront = day5_code.get_order_rules_behind_of(test_ordering_rules)

pages_to_be_printed_AFTER = day5_code.get_order_rules_infront_of(test_ordering_rules)
pages_to_be_printed_BEFORE = day5_code.get_order_rules_behind_of(test_ordering_rules)


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

# if __name__ == '__main__':
#   unittest.main()

# print(ord_rules_by_value)
# # print(f'\n\n{ord_rules_by_value.keys()}')

# for key, value in ord_rules_by_value.items():
#   print(f'KEY IS : {key} and has: {value}')
print(allowed_values)

current_update = [int(page) for page in test_updates_to_print[0].split(',')]

set_rules = {}
for page in current_update:
  set_rules[page] = set(current_update).intersection(set(allowed_values[page]['print_before']))

#sanitising the set_rules dict - removing key: set() from ^
for key,value in set_rules.items():
  if value == set():
    set_rules[key] = {}

# print(sorted(set_rules, key=lambda key: len(set_rules[key])))

ordered_update = sorted(set_rules, key=lambda key: len(set_rules[key]))
# # corrected_update = [int(page) for page in ordered_update.split(',')]
# corrected_update = [value for char in ordered_update if isinstance(char, int)]

print(f'FINAL ORDERED UPDATE IS {ordered_update}')

# print(day5_code.get_correct_ord_updates(ord_rules_by_value, test_updates_to_print))

