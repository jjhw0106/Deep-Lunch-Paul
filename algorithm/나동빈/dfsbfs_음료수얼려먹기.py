ice =  [
  [0,0,1,1,0],
  [0,0,0,1,1],
  [1,1,1,1,1],
  [0,0,0,0,0]
]
n = 4
m = 5
visited = [[False for j in range(m)] for i in range(n)]
print(visited)

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def dfs(n,m,visited):
  for e in range(n):
    for i in range(m):
      if visited[e][i] == False:
        visited[e][i] = True
      for x in range(4):
        if e+dy[x] < 0 or e+dy[x] >=n or i+dx[x] < 0 or i+dx[x]>=m:
          dfs(e+dy[x], i+dx[x], visited)
  
# def dfs():
