import itertools


number = [-3, -2, -1, 0, 1, 2, 3]
 
def solution(number):

    cnt = 0

    for e in itertools.combinations(number, 3):
        if sum(e) == 0:
            cnt += 1

solution(number)