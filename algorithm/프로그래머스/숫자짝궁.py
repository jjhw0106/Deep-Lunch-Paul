def solution(x, y):
    answer = ''

    mapX = {str(e):0 for e in range(10)}
    mapY = {str(e):0 for e in range(10)}

    k = '3'
    print(min(mapX[k], mapY[k]))

    print(mapX)    


    # if len(mapX.keys())== 1 and list(mapX.keys())[0] == 0:
    #     answer = "0"

    # print(mapX)

    return answer

solution("100","2345")