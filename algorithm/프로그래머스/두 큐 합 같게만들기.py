from collections import deque
def solution(q1, q2):
    answer = -2

    #1.
      # (q1 + q1) / 2 = goal
    #2.
      # 더 큰애에서 goal보다 크면 계속 pop
    #3.
      # goal보다 작아지면 다른 큐에서 pop시작
    q1 = deque(q1)
    q2 = deque(q2)
    q1Sum = sum(q1)
    q2Sum = sum(q2)
    goal = (q1Sum + q2Sum)/2

    count = 0
    check = len(q2)
    while 1: 
      if q1Sum == goal:
        break

      if check <= 0:
        count =-1
        break

      elif q1Sum > q2Sum:
        while q1Sum > goal:
          minus = q1.popleft()
          q1Sum -= minus
          q2Sum += minus
          q2.append(minus)
          check -= 1
          count += 1
      elif q1Sum < q2Sum:
        while q2Sum > goal:
          minus2 = q2.popleft()
          q1.append(minus2)
          q1Sum += minus2
          q2Sum -= minus2
          count += 1

    print(count)    

    return count

solution([3], [2,5])