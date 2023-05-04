# 매일 출연 -> 점수 k 번째 이내 -> 명예의 전당
k = 3
score = [10, 100, 20, 150, 1, 100, 200]

def solution(k, score):
    answer = []
    glory = []  
    for s in score:
        glory.sort(reverse =True)
        if len(glory) < k:
            glory.append(s)
        elif glory[k-1] < s:
            glory.pop()
            glory.append(s)
        glory.sort()
        answer.append(glory[0])
    print(answer)
    
    return answer

solution(k, score)


# def solution(k, score):
#     answer = []
#     q = []
#     for s in score:
#         q.append(s)
#         if len(q) > k : 
#             q.remove(min(q))
#         answer.append(min(q))
        
#     print(answer)
#     return answer
# solution(k, score)

