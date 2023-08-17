def solution(ingredient):
    answer = 0
    s = []

    for e in ingredient:
        s.append(e)
        if s[-4:] == [1,2,3,1]:
            for _ in range(4):
                s.pop()
        print(s)
    return answer


solution([2, 1, 1])