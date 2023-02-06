import random


class BaskinController :
    def __init__(self):
        self.baskin_state = 0 
        self.turn = True 
        self.callCount = 0
        self.cpuCnt = 0

    def addState(self):
        self.baskin_state += 1
        print("a")
        
    def go(self):
        self.callCount += 1
        self.baskin_state += 1
        print('baskin_state:'+str(self.baskin_state))
    
    def changeTurn(self):
        print("Turn Change!")
        self.turn = not self.turn
        self.callCount = 0
        
    def finish(self):
        print("Game End")
        print("Cpu Win!!!") if self.turn else print("You Win!!!!")
        
    def cpuGoCount(self):
        self.cpuCnt = random.randint(1,3)
        for i in range(self.cpuCnt):
            if self.baskin_state>=31:
                break
            self.go()
        