import unittest
from . import day2_code

test_input = ['7 6 4 2 1','1 2 7 8 9','9 7 6 2 1','1 3 2 4 5','8 6 4 4 1','1 3 6 7 9', '1 9 8 7 6 5', '86 80 76 73 75']


class TestDay2Code(unittest.TestCase):
  
  def test_is_safe_report(self):
    self.assertTrue(day2_code.is_safe_report(test_input[0].split()))
    self.assertFalse(day2_code.is_safe_report(test_input[1].split()))
    self.assertFalse(day2_code.is_safe_report(test_input[2].split()))
    self.assertFalse(day2_code.is_safe_report(test_input[3].split()))
    self.assertFalse(day2_code.is_safe_report(test_input[4].split()))
    self.assertTrue(day2_code.is_safe_report(test_input[5].split()))
  
  def test_dampener(self):
    self.assertTrue(day2_code.is_safe_with_dampener(test_input[0].split()))
    self.assertFalse(day2_code.is_safe_with_dampener(test_input[1].split()))
    self.assertFalse(day2_code.is_safe_with_dampener(test_input[2].split()))
    self.assertTrue(day2_code.is_safe_with_dampener(test_input[3].split()))
    self.assertTrue(day2_code.is_safe_with_dampener(test_input[4].split()))
    self.assertTrue(day2_code.is_safe_with_dampener(test_input[5].split()))
    self.assertTrue(day2_code.is_safe_with_dampener(test_input[6].split()))


if __name__ == '__main__':
  unittest.main()

# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3
