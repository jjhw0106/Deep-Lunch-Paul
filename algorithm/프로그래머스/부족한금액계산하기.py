price = 3
money = 20
count = 4
result = 10 

# 원래 이용료 : 3

def solution(price, money, count):
  answer = -1
  total = 0
  for i in range(count):
    total += (i+1)*price
  if money - total >= 0:
    return 0
  return -1 * (money - total)
  