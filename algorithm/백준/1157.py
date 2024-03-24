# input = input()
input = "Mississipi"

dic = {}
for e in input:
  if e in dic:
    dic[e] += 1
  else:
    dic[e] = 1
max, index = max(dic), dic.index(max(dic))
cnt = 0
for e in input:
  if input[e] == max:
    cnt+=1
    if cnt>=2:
      print("?")
index = dic.index(max(dic))
print(dic[index])