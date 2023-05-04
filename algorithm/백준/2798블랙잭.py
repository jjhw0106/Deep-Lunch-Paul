import itertools as iter

n, m = map(int, input().split())
cards = list(map(int, input().split()))

# n, m = [10, 500]
# cards = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]

answer = 0
cards.sort()
print(cards)

combinations = iter.combinations(cards, 3)
for e in combinations:
    if sum(e) > m:
        continue
    answer = sum(e)

print(answer)