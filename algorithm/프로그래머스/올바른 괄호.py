s= "(())()"

def solution(s):
    answer = True
    
    array = list(s)
    ansList = []
    
    idx = 0
    for e in array:
        if len(ansList) == 0:
            ansList.append(e)
            continue
        print(e + ansList[idx])
        if ansList[idx] + e == '()':
            print(ansList)
            ansList.pop
            continue
        else:
            ansList.append(e)
        idx = idx + 1    
            
    
    print(array)
    print(list.peek)

    return True

solution(s)