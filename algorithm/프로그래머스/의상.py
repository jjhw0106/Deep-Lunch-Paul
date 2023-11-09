def solution(clothes):
    answer = 1
    clothCase = {}
    
    for e in clothes:
      clothCase[e[1]] = 0
    
    for e in clothes:
      # if not clothCase[e[1]]:
      clothCase[e[1]] += 1
      # clothCase[e[1]] = e[0]
    for e in clothCase:
      answer *= (int(clothCase[e])+1)
      # answer *=int(e[1])
      print(answer-1)
    return answer -1
  
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])