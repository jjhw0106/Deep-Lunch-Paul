def solution(s):
    answer = -1

    stack = []
    top = ''
    for e in s:
        if top == e:
            stack.pop()
            if not stack:
                top = ''
            else:
                top = stack[-1]
        else: 
            stack.append(e)
            top = e
    if not stack:
        return 1
    return 0

# 재귀 풀이 -> 시간초과
#     answer = -1
#     global target
#     target = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']

#     answer = delete(s)
#     if answer == '':
#         return 1
#     return 0

# def delete(innerS):
#     check = True
#     for e in target:
#         if e in innerS:
#             innerS= innerS.replace(e,'')
#             check = False
#     if check == True:
#         return innerS
#     return delete(innerS)
    

solution('baabaas')