input = open('./Day-6/input.txt', 'r').read()

map = input.split()


class Guard():

  def __init__(self, current_position, direction, input):
    self.position = current_position
    # a DICT with {line_index: 0, index: 0}
    self.direction = direction
    self.input = input
    pass

  def next_step(self):
    if self.direction == 'N':
      return {'line_index': self.position['line_index']-1, 'index': self.position['index']}
    
    if self.direction == 'S':
      return {'line_index': self.position['line_index']+1, 'index': self.position['index']}
    
    if self.direction == 'E':
      return {'line_index': self.position['line_index'], 'index': self.position['index']+1}
    
    if self.direction == 'W':
      return {'line_index': self.position['line_index'], 'index': self.position['index']-1}
    else:
      raise Exception('Something went wrong when getting the NEXT STEP')
    pass

  def next_step_in_area(self):
    if self.direction == 'N':
      return True if 0 <= (self.position['line_index'])-1 < len(self.input) else False
    if self.direction == 'S':
      return True if 0 <= (self.position['line_index'])+1 < len(self.input) else False
    if self.direction == 'E':
      return True if 0 <= (self.position['index'])+1 < len(self.input[self.position['line_index']]) else False
    if self.direction == 'W':
      return True if 0 <= (self.position['index'])-1 < len(self.input[self.position['line_index']]) else False
    else:
      raise Exception('The guards direction is not N-S-E-W format!')

  def is_next_step_blocked(self):
    next_step = self.next_step()
    char_next_step = self.input[next_step['line_index']][next_step['index']] if self.next_step_in_area() else ''
    if char_next_step == '#' or char_next_step == 'END':
      return True
    return False
    
  pass

def get_initial_location(input):
  line_index = 0
  index = 0
  for line in input:
    index = 0
    for char in line:
      if char == "^":
        return {'line_index': line_index, 'index': index}
      index+=1
      continue
    line_index+=1
    continue
  return

def change_direction(current_direction):
  if current_direction == 'N':
    return 'E'
  if current_direction == 'S':
    return 'W'
  if current_direction == 'E':
    return 'S'
  if current_direction == 'W':
    return 'N'
  return 'DIRECTION given is not in the correct N-S-E-W format'

def get_distinct_positions(map_input):
  
  guards_start_location = get_initial_location(map_input)

  is_in_area = True
  distinct_positions = []
  guard = Guard(guards_start_location,'N', map_input)

  while is_in_area:
    is_in_area = guard.next_step_in_area()
    if guard.position not in distinct_positions:
      distinct_positions.append(guard.position)
    
    if guard.is_next_step_blocked():
      guard.direction = change_direction(guard.direction)
    guard.position = guard.next_step()

  return distinct_positions


print(f'\n⭐️ FINAL COUNT OF DISTINCT POSITIONS IS: {len(get_distinct_positions(map))}\n')