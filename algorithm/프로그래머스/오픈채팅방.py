def solution(record):
    answer = []
    
    userMap = {}
    splited = []
    for idx, e in enumerate(record):
      splited = e.split()
      if len(splited) == 3:
        userMap[splited[1]] = splited[2]
    
    for e in record:
      if e.split()[0] == 'Enter':
        answer.append(userMap[e.split()[1]] + '님이 들어왔습니다.')
      elif e.split()[0] == 'Leave':
        answer.append(userMap[e.split()[1]] + '님이 나갔습니다.')
    return answer
  
  
  
  
solution (["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])