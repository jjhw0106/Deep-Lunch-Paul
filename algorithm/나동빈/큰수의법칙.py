def solution(arr) :
    answer = 0
    arr.sort()

    big = arr[-1]
    second = arr[-2]
    count = 0
    bigcount = 0

    while count < m:
        count += 1
        bigcount += 1
        if bigcount > k:
            answer += second
            bigcount = 0
            continue
        answer += big
    print(answer)


    return answer


arr = [2, 4, 5, 4, 6]

n = 5
m = 8
k = 3

solution(arr)