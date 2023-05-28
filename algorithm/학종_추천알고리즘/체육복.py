n = 5
lost = [2,4]
reserve = [5]

def solution(n, lost, reserve):
    answer = 0
    # 학생들 번호 : 체격 순
    # 바로 뒷번호 또는 앞번호 학생에게만 빌려줄 수 있다
    # 전체 학생 수 : n
    # 도난 당한 학생 : lost[] 2,4 
    # 여벌 학생 번호 : reserve[] 1,3,5
    # lost 돌면서 reserve pop 1 ~ n번까지 돌면서, 

    for value in lost:
        print(value)
        if value in reserve:
            lost.remove(value)
            reserve.remove(value)
        elif value-1 in reserve:
            lost.remove(value)
            reserve.remove(value-1)
        elif value+1 in reserve:
            lost.remove(value)
            reserve.remove(value+1)
        
    print(lost)
        
    return answer

solution(n, lost, reserve)