def solution(n, computers):
  answer = 0
  result = 0
  m = len(computers)
  visited = [False for _ in range(n)]

  for e in range(n):
    if visited[e] == False:
      answer +=1
    
      dfs(computers, visited, e)
      
  return answer

def dfs (computers, visited, fr):
  visited[fr] = True
  
  for e in range(len(computers)):
    if computers[fr][e] == 1 and visited[e] == False:
      dfs(computers, visited, e)

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))

