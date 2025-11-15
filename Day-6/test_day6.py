import unittest
import day6_code

test_input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

test_map = test_input.split()

class TestDay5Code(unittest.TestCase):

  def test_get_initial_location(self):
    self.assertEqual(day6_code.get_initial_location(test_map), {'line_index': 6, 'index': 4})

  def test_get_distinct_positions(self):
    self.assertEqual(len(day6_code.get_distinct_positions(test_map)), 41, '❌ Distinct positions are NOT = 41')

  pass

if __name__ == '__main__':
  unittest.main()
