array = [3,56,8,8,6,4,1]

# array[0, 2] = array[2,0]

# swap
# array[0], array[2] = array[2], array[0]

# 선택정렬
# for e in range(len(array)):
#   min = array[e]
#   for i in range(e, len(array)):
#     if min > array[i]:
#       min = array[i]
#       array[e], array[i] = array[i], array[e]

# 삽입정렬
# for e in range(1, len(array)):
#   for i in range(e, 0, -1):
#     if array[i] < array[i-1]:
#       array[i] , array[i-1] =array[i-1], array[i]
# print(array)

# 퀵정렬
def quickSort(array, start, end):
  pivot = start
  left = start + 1
  right = end
  if start >= end:
    return
  while left <= right:
    while array[left] 