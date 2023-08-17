def solution(players, callings):
    answer = []
    
    playersMap = {players[i]: i+1 for i in range(len(players))}
    callingsMap = {}
    for e in callings:
        callingsMap[e] = callingsMap.get(e, 0) + 1
        

    commonKeys = playersMap.keys() & callingsMap.keys()
    print(commonKeys)
    
    result = {}
    for key in playersMap:
        if key in callingsMap:
            result[key] = playersMap[key] - callingsMap[key]
        else:
            result[key] = playersMap[key]
    
    print(result)
    # for key in commonKeys:
    #     if key in commonKeys:
    #         result[key] = playersMap[key] - callingsMap[key]

    


    return answer

solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"])