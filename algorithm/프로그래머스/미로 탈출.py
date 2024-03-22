

from collections import deque

import unittest from TestCase


def solution(maps):
  answer = 0
  m = len(maps)
  n = len(maps[0])
  q = deque()
  startIndex = getStartIndex(maps)
  leverIndex = getLeverIndex(maps)
  visited = [[False] * m for _ in range(n)]
  print(startIndex[0])
  
  q.append([startIndex[0], startIndex[1], 1])
  
  dy = [-1,1,0,0]
  dx = [0,0,-1,1]
  
  while q:
    [y,x,depth] = q.popleft()
    if maps[y][x] =="O" or maps[y][x] =="S":
      maps[y][x] = "V"
      if maps[leverIndex[0]][leverIndex[1]] == "V":
        break
      for e in range(4):02
        ny = y + dy[e]
        nx = x + dx[e]
        if ny>=0 and nx>=0 and ny<n and nx< m:
          if maps[ny][nx] == "O":
            q.append([ny, nx, depth + 1])
  print(depth)
  return answer

def getStartIndex(maps):
  for row_index, row in enumerate(maps):
    for col_index, element in enumerate(row):
      if element == 'S':
        return (row_index, col_index)
def getLeverIndex(maps):
  for row_index, row in enumerate(maps):
    for col_index, element in enumerate(row):
      if element == 'L':
        return (row_index, col_index)

solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"])