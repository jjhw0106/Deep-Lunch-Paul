s = ""

def solution(s):
    answer = ''
    if len(s) == 0:
        return ""
    t = s.lower()
    list = t.split(' ')
    
    idx = 0
    for e in list:
        print(e)
        if ord('a') <= ord(e[0]) <= ord('z'):
            temp = e[0].upper() + e[1:]
            answer += temp
        else:
            answer += e
        idx = idx + 1
        if idx == len(list):
            break
        answer += ' '
    print(answer)
    return answer   
