babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
# "aya", "ye", "woo", "ma"
def solution(babbling):
    answer = 0
    
    checkSentence = ["ayaaya","yeye","woowoo","mama"]
    for word in babbling:
        skip = False
        for check in checkSentence:
            if check in word:
                skip = True
                break
        if skip == False:
            word = word.replace("aya","1")
            word = word.replace("ye","1")
            word = word.replace("woo","1")
            word = word.replace("ma","1")
            word = word.replace("1","")
        if word == "":
            answer = answer + 1
    return answer

solution(babbling)