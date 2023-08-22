
def solution(x, y):
    answer = ''

    mapX = {str(e):0 for e in range(10)}
    mapY = {str(e):0 for e in range(10)}
    
    for c in x:
        mapX[c] += 1
    for c in y:
        mapY[c] += 1
    duplicate = 0
    for i in reversed(range(10)):
        duplicate = min(mapX[str(i)], mapY[str(i)])
        if duplicate != 0:
            answer += str(i) * duplicate
    if len(set(answer)) == 1 and list(set(answer))[0] == '0':
        answer = '0'
        
    if len(set(answer)) == 0:
        answer = '-1'

    return answer

print(solution("3","3"))