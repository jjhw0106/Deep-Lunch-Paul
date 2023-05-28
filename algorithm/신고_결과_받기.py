id_list = ["muzi", "frodo", "apeach", "neo"]
k = 2
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

def solution(id_list, report, k):
    answer = []
    reportedCnt = {}
    # 한번에 한명 신고
    # 동일 유저 신고 => 1회
    # set으로 한바퀴 돌림
    for e in id_list:
        reportedCnt[e] = 0
    noDup = list(set(report))
    banned = []
    resultMail = {}
    for e in id_list:
        resultMail[e] = 0
    
    noDupList = [r.split(' ')[1] for r in noDup]
    # k번이상 이용 정지
    for e in noDupList:
        reportedCnt[e] = reportedCnt[e]+1
    
    for e,count  in reportedCnt.items():
        if count >= k:
            banned.append(e)
        
    # print(noDup)
    # noDup의 1idx가 banned에 있으면 reported[noDup[0]에 +1]
    for e in noDup:
        target = e.split(' ')[1]
        # print(target)
        if target in banned:
            resultMail[e.split(' ')[0]] +=1
    
    for e, value in resultMail.items():
        answer.append(value)
    # print(answer)
    
    return answer


solution(id_list, report, k)