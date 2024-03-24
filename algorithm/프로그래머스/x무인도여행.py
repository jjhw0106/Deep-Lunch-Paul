def solution(maps):
  answer = []

  yLen = len(maps)
  xLen = len(maps[0])
  
  visited = [[False] * xLen for _ in range(yLen)]
  global days 
  days = 0
  
  def dfs(y, x):
    if y< 0 or y>=yLen or x<0 or x<=xLen:
      if maps[y][x] == 'X':
        return 0
      
    if visited[y][x]:
      return 0
    
    visited[y][x] = True
    global days 
    days += int(maps[y][x])
    
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)
    
  for e in range(yLen):
    for i in range(xLen):
      dfs(e,i)

solution(["X591X","X1X5X","X231X", "1XXX1"])
