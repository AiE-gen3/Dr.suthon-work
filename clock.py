import time


class Clock :
    def __init__(self, hour, minture) -> None:
        self.hour = hour
        self.minture = minture
        self.second = 0

class MintureClock(Clock):
    def __init__(self, hour, minture) -> None:
        super().__init__( hour, minture)
    
    def setMinture(self, minture):
        self.minture = minture
    
    def getMinture(self):
        return self.minture

    def countTime(self):
        self.minture += 1
        # self.second += 1
        # if ( self.second == 60 ):
            # self.minture += 1
            # self.second = 0
        if ( self.minture == 60 ):
            self.hour += 1
            self.minture = 0

if __name__ == '__main__':
    
    clock = MintureClock( 8, 49 )
    while True:
        print( f'{clock.hour}:{clock.minture}', end='\r' )
        clock.countTime()
        time.sleep(1)