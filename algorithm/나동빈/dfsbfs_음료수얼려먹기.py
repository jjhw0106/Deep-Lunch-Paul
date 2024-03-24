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

def dfs(y, x):
  if y < 0 or x < 0 or y >=n or x >= m:
    return False
  
  if ice[y][x] == 0:
    ice[y][x] = 1
    
    dfs(y-1, x)
    dfs(y, x-1)
    dfs(y+1, x)
    dfs(y, x+1)
    return True

result = 0
for e in range(n):
  for i in range(m):
    if ice[e][i] == 0:
      val = dfs(e, i)
      if val == True:
        result += 1
        
print(result)
      
  

# def dfs(y, x):
#   if y < 0 or x < 0 or y >= n or x >= m:
#     return False
  
#   if ice[y][x] == 0:
#     ice[y][x] = 1
#     print(y,x)
#     dfs(y-1, x)
#     dfs(y, x-1)
#     dfs(y+1, x)
#     dfs(y, x+1)

#     return True  
#   return False



# result = 0
# for i in range(n):
#   for e in range(m):
#     if dfs(i, e) == True:
#       result += 1

print(result)
