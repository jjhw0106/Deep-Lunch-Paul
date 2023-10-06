import itertools


from itertools import product
def solution(word):
    answer = []
    li = ['A', 'E', 'I', 'O', 'U']
    for i in range(1,6):
        for per in product(li,repeat = i):
            answer.append(''.join(per))
    answer.sort()
    return answer.index(word)+1

solution('AAAAE')
# from itertools import product


# def solution(word):
#     words = []

#     for i in range(1, 6):
#         for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
#             words.append(''.join(list(c)))

#     word.permu


#     words.sort()
#     print(words.index(word) + 1)
#     return words.index(word) + 1

