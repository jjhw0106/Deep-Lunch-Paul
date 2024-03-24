
data = [list(map(int, input().split())) for _ in range(9)]
indexY, indexX = 0, 0
max = 0
y,x = 0,0
for e in range(9):
  for i in range(9):
    if data[e][i] > max:
      max = data[e][i]
      y = e
      x = i

print(max)
print(y+1, x+1)