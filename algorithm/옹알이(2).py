
babbling = ["aya", "yee", "u", "maa"]
possible = ["aya", "ye", "woo", "ma"]

def solution(babbling):
    answer = 0
    ansStr = ""
    # babblinb 돌면서 aya, ye, woo, ma와 같은 문자열이 나오면 ""로 replace
    # 남은 길이가 0이면 +1, 아니면 no count
    # print(ansList+babbling[0].replace("ye","1"))
    # prev : 이전 발음
    for e in babbling:
        ansStr+e.replace("aya","1")
        ansStr+e.replace("Ye", "1")
    
    return answer

solution(babbling)