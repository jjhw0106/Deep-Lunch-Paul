def solution(s):
    answer = []
    splitS = list(s)
    targetDict = {}
    
    # s 돌면서 s가 not in targetDict면 targetDict에 추가
    # s가 in targetDict면 targetDict index 업데이트
    index = 0

    for c in s:
        if c not in targetDict:
            targetDict[c] = index
            answer.append(-1)
        elif c in targetDict:
            answer.append(index - targetDict[c])
            targetDict[c] = index
        index = index+1
    print(answer)
    return answer