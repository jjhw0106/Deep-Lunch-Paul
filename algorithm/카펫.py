def solution(brown, yellow):
    
    answer = []
    # y가로 * y세로 = yeloowCnt
    # 2(y가로 + y세로) + 4 = brownCnt
    
    # y 가로세로 경우의수 = [(1,24),(2,12),(3,8),(4,6)]
    yellowX = 0 # 가로길이
    yellowY = 0 # 세로길이
    
    while 1:
      yellowX += 1
      if yellow % yellowX != 0:
        continue
      yellowY = yellow / yellowX
      
      # print('x:', yellowX)
      # print(yellowY)
      if (yellowX * yellowY == yellow) and (2 * (yellowX + yellowY) + 4 == brown):
        print(yellowX, yellowY)
        break
    answer = [yellowY+2, yellowX+2]
    return answer

solution(10, 2)