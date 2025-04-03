#!/usr/bin/python3
"""qualifiers.py - A programming challenge.

Wildcards:

*                    -> Matches single character within a qualifier
- (within qualifier) -> Matches 0-8 characters within a qualifier
                     -> Also! It has to be the first or last character in the 
                     -> qualifier, otherwise it's just functioning as a hyphen. 
.-.                  -> Matches 0-22 qualifiers
"""
import unittest

def specific_pattern(pattern1, pattern2):
  """
  Given input patterns pattern1 and pattern2, with the wildcarding rules 
  described above, determine the pattern that describes the union of the 
  sets of strings described by pattern1 and pattern2.
  """
  result = ''
  quals1 = pattern1.split('.')
  quals2 = pattern2.split('.')

  # there must be 1 to 22 qualifiers in each input pattern
  assert 1 <= len(quals1) <= 22
  assert 1 <= len(quals2) <= 22

  # each qualifier must be 1 - 8 characters in length
  for q in quals1 + quals2:
    assert 1 <= len(q) <= 8

  # each character must be an uppercase letter, number, national, hyphen or star
  for c in ''.join(quals1 + quals2):
    assert c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$-*'

  # specific

  # return
  return result

def specific_qualifier(qual1, qual2):
  """
  Find the specific qualifier that matches both qual1 and qual2.
  """
  i = 0
  j = 0

  # first character is -
  if qual1[0] == '-':

  elif qual2[0] == '-':

  # last character is -

class Tests(unittest.TestCase):
  """
  """
  def test1(self):
    p1 = 'AB.CD'
    p2 = 'EF.GH'
    r = specific_pattern(p1, p2)
    assert r == ""
