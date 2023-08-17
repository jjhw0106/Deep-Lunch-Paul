def solution(people, limit):
  answer = 0
  
  people.sort(reverse=True)
  if people[0] + people[-1] > limit:
    people.pop(0)
  else : 
    people.pop(0)
    people.pop()
  print(people)
  
  # for idx, e in enumerate(people[:]):
  #   print(idx)
  #   exit.append(e)
  #   people.pop(idx)
  #   if sum(exit) > limit:
  #     answer = answer + 1
  # while(1):
  #   if len(people) == 0:
  #     print("dsfsafd")
  #   exit = []
  #   targetIdx = 0
  #   for idx, e in enumerate(people[:]):
  #     print(idx)
  #     exit.append(e)
  #     people.pop(idx)
  #     if sum(exit) > limit:
  #       answer = answer + 1
    
    
  
  # 정렬
  # 무거운 사람부터 건져올림
  
  return answer
 
solution([50,50,80,50],100) 