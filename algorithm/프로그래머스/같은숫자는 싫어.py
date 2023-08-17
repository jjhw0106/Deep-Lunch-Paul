arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    answer.append(arr[0])
    cur = arr[0]
    
    for e in range(len(arr)):
        if cur != arr[e]:
            answer.append(arr[e])
            cur = arr[e]
        
    print(answer)
    
    return answer



solution(arr)