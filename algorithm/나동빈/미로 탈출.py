from collections import deque

miro =  [
  [1,0,1,0,1,0],
  [1,1,1,1,1,1],
  [0,0,0,0,0,1],
  [1,1,1,1,1,1],
  [1,1,1,1,1,1]
]
n, m  = 5,6

q = deque()
q.append([0,0,1])
visited = [[False]*m for _ in range(n)]
count = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
while q:
  [y, x, depth] = q.popleft()
  if not visited[y][x]:
    visited[y][x] = True
    if visited[n-1][m-1]:
      break
    for e in range(4):
      ny = y + dy[e]
      nx = x + dx[e]
      print(ny, nx)
      print(depth)
      if ny >= 0 and nx >= 0 and ny < n and nx < m:
        if miro[ny][nx] == 1:
          q.append([ny, nx, depth+1])
print(depth)
