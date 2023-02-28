list = [-2, 3, 0, 2, -5]
minus_list =[]
plus_list = []
zero_list = []
# 정렬

list.sort()

for element in list:
    if element<0:
        minus_list.append(element)
    elif element == 0:
        zero_list.append(element)
    else:
        plus_list.append(element)

from itertools import permutations
# 양수 2 음수 1
sum2 = permutations(plus_list,2)
print(list(sum2))
# 양수 1 0 음수 1
# 양수 1 음수 2
# 0 0 0