from controller.baskin_controller import BaskinController
import random

controller = BaskinController()

controller.turn = random.choice([True, False])

while 1:
    if controller.baskin_state >= 31: 
        break
    if(controller.callCount>=3):  
        controller.changeTurn()
    
    if controller.turn == True:
        choice = int(input("Your Turn: "))
        if choice == 2:
            if controller.callCount == 0:
                print("한 개 이상은 외쳐야지?")
                continue
            controller.changeTurn()
        elif choice == 1:
            controller.go()
    
    elif controller.turn == False:
        print("Cpu Turn!")
        controller.cpuGoCount()
        if controller.baskin_state<31:
            controller.changeTurn()
        
    if controller.baskin_state>=31:
        controller.finish()
        

""" 
    게임시작 (while)
        탈출조건 31이면 게임끝
        my turn
            숫자 외치기 or 턴 넘기기
            외치기의 경우 3번 외치면 턴 넘겨야함
            
"""