from controller.baskin_controller import BaskinController
import random

controller = BaskinController()

while 1:
    if controller.baskin_state >= 31: 
        break
    
    if controller.yourTurn == True:
        go = int(input("Your Turn: "))
        if go == 2 or controller.callCount>=3:
            print("Turn Change!")
            controller.changeTurn()
            print(controller.yourTurn)
        elif go == 1:
            controller.go()
            print('baskin_state:'+str(controller.baskin_state))
    
    elif controller.yourTurn == False and controller.callCount<3:
        print("Cpu Turn!")
        cpuGoCnt = random.randint(1,3)
        for i in range(cpuGoCnt):
            controller.go()
            if controller.baskin_state >= 31:
                break
        print('baskin_state:'+str(controller.baskin_state))
        controller.changeTurn()

print("이겼습니다!") if controller.yourTurn1 else print("패배했습니다...")

""" 
    게임시작 (while)
        탈출조건 31이면 게임끝
        my turn
            숫자 외치기 or 턴 넘기기
            외치기의 경우 3번 외치면 턴 넘겨야함
            
"""