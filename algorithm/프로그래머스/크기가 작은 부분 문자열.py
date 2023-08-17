t = "3141592"
p = "271"
count = 0
# 부분문자열 찾기
# temp = t[0::2]
list = []
ln = len(p)
for i in range(len(t)-ln+1):
    list.append(t[i:i+ln])

for e in list:
    if int(e) <= int(p):
        count += 1

# temp = [t[i : i + len(p)] for i in range(0,len(t)-len(p),len(p))]
# 숫자로 변환
# p숫자로 변환
# 비교하면서 answerList에 추가
# answer에 length 추가