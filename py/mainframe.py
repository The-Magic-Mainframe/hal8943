#!/usr/bin/python3
"""
mainframe.py

This is a silly script that we made on stream one day.

Today I have enhanced it! I feel like I am hallucinating about something.

I think that I was banned from the CBT discord server. I'm really worried about opening up discord in my web browser right now.

Actually, I just remembered that I installed the discord app on stream the other night. Let's use that.

Yep. They removed me from both the CBT and the SZE discord servers.

This is really, really depressing.
"""
import random
import time

# choices
h = ('alive!',) * 100 + \
  ('dead.',) * 666 + \
  ('grapes.',) * 666 + \
  ('cooked.',) * 100 + \
  ('Nicholas Aaron Becker',) * 10 + \
  ('akane.',) * 10 + \
  ('sableraven.',) * 10 + \
  ('KingArvind',) * 10 + \
  ('PeterRelson050',) * 10

# loop forever
while 1:

  # predict
  r = random.randint(1, 6)
  s = ' '.join(("The mainframe is %s" % random.choice(h) for _ in range(r)))

  # emit
  for c in s:
    print(c, end='', flush=True)
    r = random.randint(1, 12)
    time.sleep(r / 720.0)

  # rest
  r = random.randint(1, 12)
  time.sleep(r / 36.0)
  print()
