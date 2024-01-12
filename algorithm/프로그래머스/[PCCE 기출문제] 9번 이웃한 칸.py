def solution(board, h, w):
  answer = 0
  
  global n
  global color
  global cnt
  
  n = len(board)
  color = board[h][w]
  cnt = 0
  
  
  val = dfs(board, h, w)
  if val == True:
    cnt += 1
  print(cnt)
  return answer


def dfs(board, h, w):
  global n
  global color
  global cnt
  if h<0 or w<0 or h>=n or w>=n:
    return False
  
  print(h, w)
  # cnt += 1 
  dfs(board, h-1, w)
  dfs(board, h, w-1)
  dfs(board, h+1, w)
  dfs(board, h, w+1)
  return True
  
  
solution ([
  ["blue", "red", "orange", "red"], 
  ["red", "red", "blue", "orange"], 
  ["blue", "orange", "red", "red"], 
  ["orange", "orange", "red", "blue"]
], 1, 1)

