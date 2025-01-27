#!/usr/bin/python3
"""
mainframe.py

This is a silly script that we made on stream one day.
"""
import random
import time

# choices
h = ('alive!',) * 10 + ('dead.',) * 100

# loop forever
while 1:

  # predict
  r = random.randint(1, 6)
  s = ' '.join(("The mainframe is %s" % random.choice(h) for _ in range(r)))

  # emit
  for c in s:
    print(c, end='', flush=True)
    r = random.randint(1, 12)
    time.sleep(r / 360.0)
  r = random.randint(1, 12)
  time.sleep(r / 6.0)
  print()
