food = [1, 3, 4, 6]
def solution(food):
    answer = ''
    # food 돌면서 홀수면 -1
    idx = 1
    
    for i in range(1, len(food)):
        e = food[i]
        print(e)
        if e % 2 == 1:
            food[i] = e - 1
            
            
    print(food)
    # answer [::-1] => 역순으로 탐색 
    return answer

solution(food)