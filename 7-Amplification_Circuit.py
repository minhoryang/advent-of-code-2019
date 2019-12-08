debug = False
def intcode_computer(array, nonblock=False, nonblock_inputs=None):
  memory = [0] * 10000
  outputs = []
  if not nonblock_inputs:
      nonblock_inputs = []
  class MemoryIndexError(IndexError): pass
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
      if nonblock:
        val = nonblock_inputs.pop(0)
        print(f"input: {val}")
      else:
        val = int(input("input: "))
      loc = memory[pos+1]
      memory[loc] = val
      return pos + 2
    elif opcode == 4:
      loc = memory[pos+1]
      output = memory[loc] if not first else loc
      outputs.append(output)
      print('print', output)
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
  return memory, pos, outputs

##############################

# Part1
import itertools

AMPLIFIER_CONTROLLER_SOFTWARE = list(map(int, "3,8,1001,8,10,8,105,1,0,0,21,42,51,76,93,110,191,272,353,434,99999,3,9,1002,9,2,9,1001,9,3,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1002,9,3,9,4,9,99,3,9,1002,9,4,9,101,5,9,9,1002,9,3,9,1001,9,4,9,1002,9,5,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,5,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99".split(',')))

max_thruster_signal = 0
max_phase_setting_sequences = None
for phase_setting_sequences in itertools.permutations(range(5)):
  inputs = [0, 0]
  for phase_setting_sequence in phase_setting_sequences:
    inputs[0] = phase_setting_sequence
    _, _, outputs = intcode_computer(AMPLIFIER_CONTROLLER_SOFTWARE.copy(), nonblock=True, nonblock_inputs=inputs.copy())
    print(outputs)
    inputs[1] = outputs[0]
  current_thruster_signal = inputs[1]
  if current_thruster_signal > max_thruster_signal:
    max_thruster_signal = current_thruster_signal
    max_phase_setting_sequences = phase_setting_sequences

print(max_thruster_signal, max_phase_setting_sequences)
