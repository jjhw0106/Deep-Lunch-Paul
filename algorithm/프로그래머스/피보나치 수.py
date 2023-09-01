
def solution(n):
    answer = 0
    return fibo(n)%1234567
  
def fibo(n):
  temp = 0
  start = 0
  second = 1
  for _ in range(1, n):
    temp = start + second
    start = second
    second = temp
    # print(temp)

  return temp
  
solution(100000)
