food = [1, 3, 4, 6]
def solution(food):
    answer = ''
    food.pop(0)
    for idx, value in enumerate(food):
        if value%2 == 1:
            value -= 1
        for e in range(int(value/2)):
            answer += str(idx+1)
    reverse = answer[::-1]
    print(reverse)
    answer = answer + '0' + reverse

    print(answer)

    return answer

solution(food)