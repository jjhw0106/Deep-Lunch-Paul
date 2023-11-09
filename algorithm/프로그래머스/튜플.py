def solution(s):
    answer = []
    splited = s.split("},")
    for e in splited:
      answer.append(e.replace("{", "").replace("}", ""))
      answer.sort(key=len)
      
    answer2 = []
    for e in answer:
      for i in list(e.split(",")):
        if i not in answer2:
          answer2.append(i)
    return list(map(int, answer2))
    # print(answer2)
    # print(list(map(int,answer2)))
    
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")