# prompt: print um jogo de cara ou coroa

import random

flip = random.randint(0, 1)

if flip == 0:
  print("Cara")
else:
  print("Coroa")
