# 최고점 : k 최저점 : 1
# 사과 점수 p -> 제일 싼 사과 / m개
# 사과들 점수 score
score = [1, 2, 3, 1, 2, 3, 1]
m = 4
k = 3

# , 1, 2, 2,  1, 2, , 2
# 444 444 222 112
# 12  12  6   3

def solution(k, m, score):
    answer = 0

    # 가장 높은거부터 pop
    score.sort(reverse = True)
    print(score)

    return answer

solution(k,m,score)