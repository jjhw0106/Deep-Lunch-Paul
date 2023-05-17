k = 4 # 최상품 사과
m = 3 # 한상자에 m개
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

def solution(k, m, score):
    answer = 0
    sell = []
    # 정렬
    # 큰거부터 set구성
    score.sort()
    
    while len(score) >= m:
        for i in range(m):
            sell.append(score.pop())
            if len(sell) == m:
                answer = answer + (min(sell) * m)
                sell = []
                
    
    return answer

solution(k, m, score)