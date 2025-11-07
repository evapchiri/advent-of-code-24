input = open('./Day-4/input.txt', 'r').read()

splitted_input = input.split('\n')

# for line in splitted_input:
#   print(len(line))


# CREATE A CLASS TO FIND NEXT CHARACTER

class SurroundingChar():

  def __init__(self, index, line_index, line, input, offset):
    self.line = line
    self.index = index
    self.fullCrossword = input
    self.line_index = line_index
    self.offset = offset
    self.NextLetter = line[index + offset] if (0<= index + offset < len(line)) else ''
    self.PrevLetter = line[index - offset] if (0<= index - offset < len(line)) else ''
    self.TopLetter = input[line_index-offset][index] if (0 <= line_index - offset < len(input)) and ( 0<= index < len(line)) else ''
    self.BottomLetter = input[line_index+offset][index] if line_index + offset < len(input) and ( 0<= index < len(line)) else ''
    self.DiagTopLeftLetter = input[line_index-offset][index-offset] if (0 <= line_index - offset < len(input)) and ( 0<= index - offset < len(line)) else ''
    self.DiagTopRightLetter = input[line_index-offset][index+offset] if (0 <= line_index - offset < len(input)) and (0 <= index + offset < len(line)) else ''
    self.DiagBotLeftLetter = input[line_index+offset][index-offset] if (0 <= line_index + offset < len(input)) and (0 <= index - offset < len(line)) else ''
    self.DiagBotRightLetter = input[line_index+offset][index+offset] if (0 <= line_index + offset < len(input)) and (0 <= index + offset < len(line)) else ''
    
    pass

  def SurroundingLetters(self):
    """
    Gives back / updates a dict of all surrounding letters of the character.
    """
    return {
      'NextLetter': self.NextLetter,
      'PrevLetter': self.PrevLetter,
      'TopLetter': self.TopLetter,
      'BottomLetter': self.BottomLetter,
      'DiagTopLeftLetter': self.DiagTopLeftLetter,
      'DiagTopRightLetter': self.DiagTopRightLetter,
      'DiagBotLeftLetter': self.DiagBotLeftLetter,
      'DiagBotRightLetter': self.DiagBotRightLetter
    }


def XMAS_count(input):

  hit_word = 'XMAS'

  count_XMAS = 0 
  line_index = 0
  for line in input:
    i = 0
    for char in line:
      surrounding_words = {
      'NextLetter': '',
      'PrevLetter': '',
      'TopLetter': '',
      'BottomLetter': '',
      'DiagTopLeftLetter': '',
      'DiagTopRightLetter': '',
      'DiagBotLeftLetter': '',
      'DiagBotRightLetter': ''
      }
      if char == hit_word[0]: # when 'X' is found..
        char = SurroundingChar(i, line_index, line, input, 0)
        surrounding_words.update(char.SurroundingLetters())
        for num in range(1,4):
          char = SurroundingChar(i, line_index, line, input, num)
          next_surrounding_letters = char.SurroundingLetters()
          for key,value in surrounding_words.items():
            surrounding_words.update({key : value + (next_surrounding_letters[key])})
      i += 1
      count_XMAS += (list(surrounding_words.values())).count('XMAS')
    line_index += 1

  # print(count_XMAS)
  print(f'⭐️⭐️ Final count of XMAS is {count_XMAS}')
  return count_XMAS

XMAS_count(splitted_input)




# print(splitted_input[0][0])

