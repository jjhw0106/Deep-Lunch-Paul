import itertools
from typing import Type

def solution(numbers):
    answer = 0
    
    # 모든 경우의 수
    
    # for 모든경우의 수
      # 소수판별
    allCase = []
    count = 0
    for e in range(len(numbers)+1):
      element = itertools.permutations(numbers, e)
      for r in element:
        allCase.append(''.join(r))
    for e in set(allCase):
      if e != '':
        if e[0] == '0' or e == '1':
          continue
        if e == '2':
          answer += 1
          continue
        if sosuCheck(int(e)):
          answer += 1
    print(answer)
    return answer
  
  
def sosuCheck(number):
  target = number**(1/2)
  for e in range(int(target)):
    divider = e+2
    if number%divider == 0:
      return False
  return True

solution('27')