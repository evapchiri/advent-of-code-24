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
    Gives back / updates a dict of all surrounding letters of the character in the current offset.
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
  print(f'\n⭐️ Final count of XMAS is {count_XMAS}\n')
  return count_XMAS

XMAS_count(splitted_input)


def countingX_MAS(input):
  hit_word = 'MAS'
  count_X_MAS = 0 
  line_index = 0
  surrounding_letters = {
      'NextLetter': '',
      'PrevLetter': '',
      'TopLetter': '',
      'BottomLetter': '',
      'DiagTopLeftLetter': '',
      'DiagTopRightLetter': '',
      'DiagBotLeftLetter': '',
      'DiagBotRightLetter': ''
      }
  for line in input:
    i = 0
    for char in line:
      if char == hit_word[1]: # when 'A' is found this time ..
        char = SurroundingChar(i, line_index, line, input, 1)
        surrounding_letters = char.SurroundingLetters()
        hit_TopLtoBotR = True if ('M','S') == (surrounding_letters['DiagTopLeftLetter'],surrounding_letters['DiagBotRightLetter']) else False
        hit_TopRtoBotL = True if ('M','S') == (surrounding_letters['DiagTopRightLetter'],surrounding_letters['DiagBotLeftLetter']) else False
        hit_BotRtoTopL = True if ('M','S') == (surrounding_letters['DiagBotRightLetter'],surrounding_letters['DiagTopLeftLetter']) else False
        hit_BotLtoTopR = True if ('M','S') == (surrounding_letters['DiagBotLeftLetter'],surrounding_letters['DiagTopRightLetter']) else False
        count_X_MAS += 1 if ([hit_TopLtoBotR,hit_TopRtoBotL,hit_BotRtoTopL,hit_BotLtoTopR].count(True) == 2) else 0
      i += 1

    line_index += 1 

  print(f'\n⭐️⭐️ Final count of X-MAS is {count_X_MAS}\n')

  return count_X_MAS

countingX_MAS(splitted_input)

