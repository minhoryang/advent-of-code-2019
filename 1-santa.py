# https://adventofcode.com/2019/day/1 by Minho Ryang

import math

a = [
  # input numbers ...
]


def _(a):
  return math.floor(a / 3) - 2


print("question1", sum(map(_, a)))


def _(a):
  b = math.floor(a / 3) - 2
  if b > 0:
    return _(b) + b
  return 0


print("question2", sum(map(_, a)))
