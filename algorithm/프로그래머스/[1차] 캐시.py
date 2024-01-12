def solution(cacheSize, cities):
    answer = 0
    
    # deque(maxlen, ) => 덱에 max보다 크면 
    # cache 0 일경우 체크해보기
    cache = []
    while 1:
      if len(cities) == 0:
        break
      e = cities.pop(0).lower()
      if e not in cache:
        answer += 5
        cache.append(e)
        if len(cache) > cacheSize:
          cache.pop(0)
      else:
        cache.append(cache.remove(e))
        answer += 1
    print(answer)
    return answer 
  
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])