data = list(map(int, input().split()))
n = data[0]
m = data[1]

# 1 선언 후 한줄 씩 초기화
# a, b = [], []

# for e in range(n):
#   a.append(list(map(int, input().split())))
# for e in range(n):
#   b.append(list(map(int, input().split())))

# 2 선언과 초기화 동시에
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]


c = [[0] * m for _ in range(n)]
for e in range(n):
  for i in range(m):
    c[e][i]=(a[e][i] + b[e][i])

for e in c:
  # print(' '.join(map(str, e)))
  print(*e)


# for e in range(n):

#   a = list(map(int, input().split()))
