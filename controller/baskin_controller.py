class BaskinController :
    
    def __init__(self):
        self.baskin_state = 0 
        self.yourTurn = True 
        self.callCount = 0

    def addState(self):
        self.baskin_state += 1
        print("a")
        
    def go(self):
        self.callCount += 1
        self.baskin_state += 1
    
    def changeTurn(self):
        self.yourTurn = not self.yourTurn
        self.callCount = 0