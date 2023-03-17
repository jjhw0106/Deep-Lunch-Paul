targetIdx =0
curIdx1 = 0
curIdx2 = 0
goal = ["i", 'want', 'to', 'drink', 'water']
cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
answer = ""

while 1:
    if targetIdx >= len(goal):
        answer = "yes"
        break
    if  curIdx1<len(cards1) and cards1[curIdx1] == goal[targetIdx] : 
        curIdx1 = curIdx1+1
        targetIdx = targetIdx+1
    elif curIdx2<len(cards2) and cards2[curIdx2] == goal[targetIdx] :
        curIdx2 = curIdx2+1
        targetIdx = targetIdx+1
    else:
        answer = "no"
        break
    
print(answer)
        