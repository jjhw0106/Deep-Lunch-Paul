n = 20 # 총 빈병 
a = 2 # 교환 빈병
b = 1 # 콜라

# 콜라 get -> answer ++
# 빈병 ++

def solution(a, b, n):
    answer = 0
    while n>=a:
        answer += int(n/a) * b
        n = int(n%a) + int(n/a)*b

    print(answer)
    return answer

solution(a,b,n)