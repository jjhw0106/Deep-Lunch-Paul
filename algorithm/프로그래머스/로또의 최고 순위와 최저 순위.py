lottos = [44, 1, 0, 0, 31, 25]
win_nums = 	[31, 10, 45, 1, 6, 19]


def solution(lottos, win_nums):
    answer = []
    index = 0
    certainCnt = 0
    min = 0
    max = 0
    
    for l in lottos:
        if l in win_nums:
            lottos[index] = 0
            certainCnt += 1
        index += 1
    max = lottos.count(0)
    min = certainCnt
    
    def getRank(bingo):
        if bingo <= 1:
            return 6
        elif bingo == 2:
            return 5
        elif bingo == 3:
            return 4
        elif bingo == 4:
            return 3
        elif bingo == 5:
            return 2
        elif bingo == 6:
            return 1
    
    answer.append(getRank(max))
    answer.append(getRank(min))
    print(answer)
    return answer



solution(lottos, win_nums)