from unittest import TestCase
from collections import deque

def solution(maps):
  answer = 0
  m = len(maps)
  n = len(maps[0])
  startPos = ()
  endPos = ()
  posCheck = 0
  q = deque()

  def findPos():
    nonlocal startPos, endPos, posCheck
    for e in range(m):
      for i in range(n):
        if maps[e][i] == 'S':
          startPos = (e, i)
          posCheck += 1
        if maps[e][i] == 'E':
          endPos = (e, i)
          posCheck += 1
        if posCheck == 2:
          return
  findPos()
  
  q.append(startPos)
  dy = [0,0,-1,1]
  dx = [-1,1,0,0]

  while(q):
    (y,x) = q.popleft()
    ny, nx = y + dy, x + dx
    if not (ny < 0 or ny > m or nx < 0 or nx > n):
      if maps[ny][nx] == "L":
        
  return answer



solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])

# class TestStringMethods(unittest.TestCase):

#   def test_upper(self):
#     self.assertEqual('foo'.upper(), 'FOO')

#   def test_isupper(self):
#     self.assertTrue('FOO'.isupper())
#     self.assertFalse('Foo'.isupper())

#   def test_split(self):
#     s = 'hello world'
#     self.assertEqual(s.split(), ['hello', 'world'])
#     # check that s.split fails when the separator is not a string
#     with self.assertRaises(TypeError):
#       s.split(2)

# unittest.solution()