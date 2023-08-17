# xyz => 10일 회원
# 한개 할인 하루 한개
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1] # 합 : 10
discount = ["chicken", "apple", "apple", 
            "banana", "rice", "apple", 
            "pork", "banana", "pork", 
            "rice", "pot", "banana", 
            "apple", "banana"]

def solution(want, number, discount):
    answer = 0
    # pick10
    first = 0       
    # for want
    #     count element
    # count element == 10 
    # answer += 1

    while(1):
        productMap = dict()
        for idx in range(len(number)):
            productMap[want[idx]] = number[idx]

        if first+10 > len(discount):
            break
        pick = discount[first:first+10]
        first += 1

        
        print((pick))

    return answer

solution(want, number, discount)