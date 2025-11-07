import unittest
import day4_code


# test_input = 'MMMSXXMASM\nMSAMXMSMSA\nAMXSXMAAMM\nMSAMASMSMX\nXMASAMXAMM\nXXAMMXXAMA\nSMSMSASXSS\nSAXAMASAAA\nMAMMMXMMMM\nMXMXAXMASX'

test_input = """
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

test_input_rob = """
AXC
DEF
GHI
""".strip()

splitted_input = test_input.split('\n')

class TestDay4Code(unittest.TestCase):

  def test_XMAS_count(self):
    self.assertEqual(day4_code.XMAS_count(splitted_input), 18, 'XMAS count was not 18!!! :( ')


if __name__ == '__main__':
  unittest.main()
3



