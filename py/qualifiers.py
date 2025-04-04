#!/usr/bin/python3
"""qualifiers.py - A programming challenge.

Wildcards:

*                    -> Matches single character within a qualifier
- (within qualifier) -> Matches 0-8 characters within a qualifier
                     -> Also! It has to be the first or last character in the 
                     -> qualifier, otherwise it's just functioning as a hyphen. 
.-.                  -> Matches 0-22 qualifiers
"""
import re
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

  # convert patterns to regular expressions

  # return
  return result

class Tests(unittest.TestCase):
  """
  Unit tests.
  """
  def test1(self):
    p1 = 'AB.CD'
    p2 = 'EF.GH'
    r = specific_pattern(p1, p2)
    assert r == ""

  def test2(self):
    p1 = 'NICK.BECKER'
    p2 = 'N-.B-'
    r = specific_pattern(p1, p2)
    assert r == 'NICK.BECKER'

  def test3(self):
    p1 = 'NICK.-.BEC-ER'
    p2 = '*ICK.MOTHER.TRUCKING.BEC-ER'
    r = specific_pattern(p1, p2)
    assert r == 'NICK.MOTHER.TRUCKING.BEC-ER'

  def test4(self):
    """
    This is a nice test. Thanks, @acf2sme from Twitch.
    """
    p1 = '*-.-'
    p2 = 'NICK.I-.-'
    p3 = 'N-.*S.SLOW'
    r12 = specific_pattern(p1, p2)
    assert r12 == 'NICK.I-.-'
    r13 = specific_pattern(p1, p3)
    assert r13 == 'N-.*S.SLOW'
    r23 = specific_pattern(p2, p3)
    assert r23 == 'NICK.IS.SLOW'
    r1213 = specific_pattern(r12, r13)
    r1223 = specific_pattern(r12, r23)
    r1323 = specific_pattern(r13, r23)
    assert r1213 == r1223 == r1323 == 'NICK.IS.SLOW'
