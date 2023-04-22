name = ["kali", "mari", "don"]
yearning = [11, 1, 55]
photo = [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]



def solution():
    dictScore = {}
    answer = []
    for n, y in zip(name, yearning):
        dictScore[n] = y
    
    for i in photo:
        sum = 0
        for j in i:
            if j in dictScore:
                sum += dictScore[j]
        answer.append(sum)

    print(answer)
    return answer

solution()