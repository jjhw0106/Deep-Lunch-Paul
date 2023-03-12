import random

attempt = 0

def compare():
    print(cpuNum)
    if int(userNum) == int(cpuNum) : print(str(attempt)+'회만에 맞췄습니다!')
    elif int(userNum) > int(cpuNum) : print("Down")
    else: print("Up")
    
# Computer pick a number
cpuNum : int = random.randint(1,100)

while(1):
    # User input a number
    userNum : int = input("숫자를 고르세요: ")
    attempt += 1    
    
    # 외친 숫자 == 컴퓨터 Pick => finish
    if int(userNum) == int(cpuNum):
        print(str(attempt)+'회만에 맞췄습니다!')
        break
    else:
        compare()
    