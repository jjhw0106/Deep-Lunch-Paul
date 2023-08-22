def solution(n):
  answer = 0
  
  checkNum = 0
  start = 1
  
  while 1:
    if start > n/2:
      break
    for e in range(n):
      checkNum += (start + e)
      if checkNum >= n:
        start += 1
        break
    if checkNum == n:
      answer += 1
    checkNum = 0
  return answer+1
  
solution(15)