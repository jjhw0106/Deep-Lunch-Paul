from collections import defaultdict


name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

def solution(name, yearning, photo):
    # name : 그리워하는 사람의 이름
    # yearning : 그리움 점수
    # photo : 분석대상 사진
    
    result = {}
    answer = []
    sum = 0
    for name, yearning in zip(name, yearning):
        result[name] = yearning
    
    name_info = defaultdict(int)
    
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            if(photo[i][j] in name):
                sum += result[photo[i][j]]
    print(sum)
    return answer   

solution(name, yearning, photo)