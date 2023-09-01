# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

# 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.


def solution(n):
    answer = 0
    small = -1
    big = -1
    two = list(tenToTwo(n))
    for index, e in enumerate(reversed(two)):
      if e == 0 and small != -1:
        big = index
      if e == 1 and small == -1:
        small = index
      print(big, small)
      two[big], two[small] = two[small], two[big]
      if(big != -1 and small != -1):
        break
        
    print(two)
    target = 0
    # 첫번째 1과 첫번째 0을 바꾼다
    
      
    # 2 to 10
    # 10 to 2
    # 오른쪽부터 1 체크, 0나오면 1로 바꾸고 직전 1을 0으로 변경
    # 첫자리가 0이면 그냥 1로 변경
    # 전부 1이면 마지막 1 0으로 변경 후 맨 왼쪽에 1 추가
    tenToTwo(n)
    
    
    return answer
  
def tenToTwo(n):
  result = ''
  while 1:
    if n == 1:
      result = str(int(n)) + result
      break
    if n == 0:
      break
    result = str(int(n % 2)) + result
    n = int(n/2)
  return result
  
solution(78)

