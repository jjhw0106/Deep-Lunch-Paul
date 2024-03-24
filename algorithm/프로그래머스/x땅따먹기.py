def solution(land):
  answer = 0
  
  start = max(land[0])
  sum = 0
  posIndex = -1
  
  for e in land:
    posValue = max([e[i] for i in range(len(e)) if i != posIndex])
    posIndex = e.index(posValue)
    print(posValue)
    sum += posValue
  print(sum)

  return answer


solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]])