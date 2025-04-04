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
  result = []
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
  regexp1 = pattern_to_regexp(quals1)
  print(f'p: {pattern1}')
  print(f'r: {regexp1}')
  regexp2 = pattern_to_regexp(quals2)
  print(f'p: {pattern2}')
  print(f'r: {regexp2}')

  # negate (complement) the regular expressions
  #negated1 = negated_regexp(regexp1)
  #negated2 = negated_regexp(regexp2)

  # intersect the regular expressions by joining the complements (De Morgan!!!)
  #intersection = f'({negated1}|{negated2})'

  # compile the intersected regular expression
  #compiled = re.compile(intersection)

  # convert the compiled regular expression into pattern language
  #result = regexp_to_pattern(compiled)

  # return
  return ''.join(result)

def pattern_to_regexp(quals):
  """
  Convert the input pattern (specified as a list of qualifiers)
  to an equivalent regular expression.
  """
  result = []
  for q in quals:

    # qualifier is a single hyphen (wildcard)?
    if q == '-':
      result.append(r'[A-Z0-9@#$-]{1,8}')

    # qualifier ends in a hyphen (wildcard)?
    elif q[-1] == '-':
      result.append(q[:-1] + r'[A-Z0-9@#$-]{1,%d}' % (9 - len(q)))

    # qualifier ends with asterisk(s) (wildcard)?
    elif q[-8:] == '********':
      result.append(r'[A-Z0-9@#$-]{1,8}')
    elif q[-7:] == '*******':
      result.append(q[:1] + r'[A-Z0-9@#$-]{1,7}')
    elif q[-6:] == '******':
      result.append(q[:2] + r'[A-Z0-9@#$-]{1,6}')
    elif q[-5:] == '*****':
      result.append(q[:3] + r'[A-Z0-9@#$-]{1,5}')
    elif q[-4:] == '****':
      result.append(q[:4] + r'[A-Z0-9@#$-]{1,4}')
    elif q[-3:] == '***':
      result.append(q[:5] + r'[A-Z0-9@#$-]{1,3}')
    elif q[-2:] == '**':
      result.append(q[:6] + r'[A-Z0-9@#$-]{1,2}')
    elif q[-1:] == '*':
      result.append(q[:7] + r'[A-Z0-9@#$-])')

    # no trailing wildcards
    else:
      result.append(q)

  # deal with single character wildcards (asterisks)
  return '\.'.join(result).replace('*', r'[A-Z0-9@#$-]')

def negated_regexp(regexp):
  """
  Negate the given regular expression. Use a negative lookahead, probably.
  """
  raise NotImplementedError()

def regexp_to_pattern(regexp):
  """
  Convert the input regular expression to an equivalent pattern. ???
  """
  raise NotImplementedError()

class Tests(unittest.TestCase):
  """
  Here are the unit tests.
  """
  def test1(self):
    p1 = 'AB.CD'
    p2 = 'EF.GH'
    r = specific_pattern(p1, p2)
    #assert r == ""

  def test2(self):
    p1 = 'NICK.BECKER'
    p2 = 'N-.B-'
    r = specific_pattern(p1, p2)
    #assert r == 'NICK.BECKER'

  def test3(self):
    p1 = 'NICK.-.BEC-ER'
    p2 = '*ICK.MOTHER.TRU**ING.B*C-ER'
    r = specific_pattern(p1, p2)
    #assert r == 'NICK.MOTHER.TRUCKING.BEC-ER'

  def test4(self):
    """
    This is a nice test. Thanks, @acf2sme from Twitch.
    """
    p1 = '*-.-'
    p2 = 'NICK.I-.-'
    p3 = 'N-.*S.SLOW'
    r12 = specific_pattern(p1, p2)
    #assert r12 == 'NICK.I-.-'
    r13 = specific_pattern(p1, p3)
    #assert r13 == 'N-.*S.SLOW'
    r23 = specific_pattern(p2, p3)
    #assert r23 == 'NICK.IS.SLOW'
    #r1213 = specific_pattern(r12, r13)
    #r1223 = specific_pattern(r12, r23)
    #r1323 = specific_pattern(r13, r23)
    #assert r1213 == r1223 == r1323 == 'NICK.IS.SLOW'
  
  def test5(self):
    p1 = 'NICK.******.**.***.****.*.BECKER'
    p2 = 'N-.IS.LOSING.HIS.MIND.LOL.BECKER'
    r = specific_pattern(p1, p2)
    #assert r == 'NICK.ROC-KER.BOCKER'
