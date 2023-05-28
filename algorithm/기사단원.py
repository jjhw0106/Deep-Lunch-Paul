def solution(number, limit, power):
    answer = 0
    #number : 기사단원의 수 // 번호 (약수의 개수가 기사의 무기)
    #limit : 파워 제한
    #power : 제한초과 기사가 사용할 무기
    
    # 기사의 파워(약수의 개수)구하기
    

    for e in range(number):
        a = e+1
        # print(getSubCnt(a))
        if getSubCnt(a) <= limit:
            answer = answer + getSubCnt(a)
        else:
            answer = answer + power
        print(answer)

    return answer

def getSubCnt(num):
    cnt = 0
    for e in range(num):
        if num % (e+1) == 0:
            cnt = cnt + 1
    return cnt
solution(10, 3, 2)