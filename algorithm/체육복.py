# 체격순
# 바로앞 or 바로뒤
# 최대한 많은 학생이 체육수업
# n : 전체학생수
# lost : 체육복 도난
# reserve : 여벌 학생

n = 5
lost = [1,2,3]
reserve = [2,3,4]

def solution(n, lost, reserve):
    answer = 0
    # [2, 3, 4, 5]
    # lost n번 -> reserve n? reserve n-1 ? reserve n+1 ?
    index = 0
    lost.sort()
    while index < len(lost):
        l = lost[index]
        if l in reserve:
            reserve.remove(l)
            lost.remove(l)
            continue
        index += 1
        
    index = 0
    while index < len(lost):
        print('lost {}', lost)
        print('reserve {}', reserve)
        print("index {}", index)
        l = lost[index]
        # if l in reserve:
        #     reserve.remove(l)
        #     lost.remove(l)
        #     continue
        if l-1 in reserve:
            reserve.remove(l-1)
            lost.remove(l)
            continue
        if l+1 in reserve:
            reserve.remove(l+1)
            lost.remove(l)
            continue
        index += 1
    answer = n - len(lost)
    print(answer)
    return answer

solution(n, lost, reserve)
    # for l in lost:
    #     print(l)
        # if l in reserve:
        #     reserve.remove(l)
        #     lost.remove(l)
        #     print(1)
        #     continue
        # if l-1 in reserve:
        #     reserve.remove(l-1)
        #     lost.remove(l)
        #     print(2)
        #     continue
        # if l+1 in reserve:
        #     reserve.remove(l+1)
        #     lost.remove(l)
        #     print(3)
