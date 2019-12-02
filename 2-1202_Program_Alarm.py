memory = [0] * 10000

def intcode_computer(array):
  def _(pos):
    intcode = memory[pos]
    if intcode == 1:
      val1 = memory[memory[pos+1]]
      val2 = memory[memory[pos+2]]
      loc = memory[pos+3]
      memory[loc] = val1 + val2
      return pos + 4
    elif intcode == 2:
      val1 = memory[memory[pos+1]]
      val2 = memory[memory[pos+2]]
      loc = memory[pos+3]
      memory[loc] = val1 * val2
      return pos + 4
    elif intcode == 99:
      return -1
    raise Exception(f'{pos} {intcode}')
  for idx, data in enumerate(array):
    memory[idx] = data
  pos = 0
  while pos>=0:
    pos = _(pos)

part1 = [
  # numbers ...
]
part1[1] = 12
part1[2] = 2

intcode_computer(part1)
print(memory[0])

##############################

import random
rnd_memory = []
def rnd():
  a, b = random.choice(range(100)), random.choice(range(100))
  if len(rnd_memory) >= 10000:
    raise Exception('exceed')
  elif (a, b) in rnd_memory:
    return rnd()
  rnd_memory.append((a, b))
  return (a, b)

while True:
  memory = [0] * 10000
  part2 = part1.copy()
  a, b = rnd()
  part2[1], part2[2] = a, b
  intcode_computer(part2)
  if memory[0] == 19690720:
    raise Exception(f'found! {a} {b}')
