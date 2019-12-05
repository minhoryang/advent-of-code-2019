memory = [0] * 10000
debug = False
def intcode_computer(array):
  def _(pos):
    intcode = str(memory[pos] + 100000)
    first = int(intcode[-3])
    second = int(intcode[-4])
    third = int(intcode[-5])
    opcode = int(intcode[-2:])
    if debug:
        print(memory[:12])
        print(f'{pos} {intcode[1:]} {opcode} {first} {second} {third}')
    if opcode == 1:
      val1 = memory[memory[pos+1]] if not first else memory[pos+1]
      val2 = memory[memory[pos+2]] if not second else memory[pos+2]
      loc = memory[pos+3]
      memory[loc] = val1 + val2
      return pos + 4
    elif opcode == 2:
      val1 = memory[memory[pos+1]] if not first else memory[pos+1]
      val2 = memory[memory[pos+2]] if not second else memory[pos+2]
      loc = memory[pos+3]
      memory[loc] = val1 * val2
      return pos + 4
    elif opcode == 3:
      if first:
          raise
      val = int(input())
      loc = memory[pos+1]
      memory[loc] = val
      return pos + 2
    elif opcode == 4:
      loc = memory[pos+1]
      print('print', memory[loc] if not first else loc)
      return pos + 2
    elif opcode == 5:  # jump-if-true
      val1 = memory[memory[pos+1]] if not first else memory[pos+1]
      val2 = memory[memory[pos+2]] if not second else memory[pos+2]
      if debug:
        print(val1, val2)
      if val1 != 0:
        return val2
      return pos + 3
    elif opcode == 6:  # jump-if-false
      val1 = memory[memory[pos+1]] if not first else memory[pos+1]
      val2 = memory[memory[pos+2]] if not second else memory[pos+2]
      if debug:
        print(val1, val2)
      if val1 == 0:
        return val2
      return pos + 3
    elif opcode == 7:  # less-than
      val1 = memory[memory[pos+1]] if not first else memory[pos+1]
      val2 = memory[memory[pos+2]] if not second else memory[pos+2]
      val3 = memory[pos+3]
      if third:
        raise
      if debug:
        print(val1, val2, val3)
      memory[val3] = 1 if val1 < val2 else 0
      return pos + 4
    elif opcode == 8:  # equals
      val1 = memory[memory[pos+1]] if not first else memory[pos+1]
      val2 = memory[memory[pos+2]] if not second else memory[pos+2]
      val3 = memory[pos+3]
      if third:
        raise
      if debug:
        print(val1, val2, val3)
      memory[val3] = 1 if val1 == val2 else 0
      return pos + 4
    elif opcode == 99:
      return -1
    raise Exception(f'{pos} {intcode[1:]} {opcode}')
  for idx, data in enumerate(array):
    memory[idx] = data
  pos = 0
  while pos>=0:
    pos = _(pos)

##############################
