import unittest
import day4_code


# test_input = 'MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX'

test_input_pt1 = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()

test_input_small = """
AXC
DEF
GHI
""".strip()

test_input_pt2 = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
""".strip()

test_input_pt2_small = """
.M.S.
..A..
.M.S.
"""

splitted_input_pt1 = test_input_pt1.split('\n')
splitted_input_pt2 = test_input_pt2.split('\n')

class TestDay4Code(unittest.TestCase):

  def test_XMAS_count(self):
    self.assertEqual(day4_code.XMAS_count(splitted_input_pt1), 18, 'XMAS count was not 18!!! :( ')

  def test_counting_X_MAS(self):
    self.assertEqual(day4_code.countingX_MAS(splitted_input_pt2), 9, 'X-MAS count was not 9!!! :( ')

if __name__ == '__main__':
  unittest.main()




