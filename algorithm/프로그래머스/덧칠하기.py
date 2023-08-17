# 벽 n미터 
# section : 빵꾸 번호
# n : 구역 길이 n
# m : 롤러의 길이

n = 4
m = 1
section = [1,2,3,4]
background = [True]*n
for e in range(len(background)):
    if e+1 in section:
        background[e] = False
print(background)

count = 0
for e in range(len(background)):
    print(background[e])
    if background[e] == False:
        # print("fff")
        if e+m > n:
            continue
        background[e:e+m] = [True]*m
        count = count+1
if False in background:
    count=count+1
print(count)   

def solution(n, m, section):
    background = [True]*n
    for e in range(len(background)):
        if e+1 in section:
            background[e] = False
    print(background)

    count = 0
    for e in range(len(background)):
        print(background[e])
        if background[e] == False:
            # print("fff")
            if e+m > n:
                continue
            background[e:e+m] = [True]*m
            count = count+1
    if False in background:
        count=count+1
        print(count)
    
    return count