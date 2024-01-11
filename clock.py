import time

class NumberDisplay:
    def __init__(self, initValue):
        self.v = initValue

    def tick(self):
        self.v = (self.v + 1) % 60

class ClockDisplay:
    def __init__(self, hourValue, minuteValue):
        self.hour = NumberDisplay(hourValue)
        self.minute = NumberDisplay(minuteValue)

    def tick(self):
        self.minute.tick()
        if self.minute.v == 0:
            self.hour.tick()

    def run(self):
        while True:
            print(f"{self.hour.v:02d}:{self.minute.v:02d}", end='\r')
            time.sleep(1)
            self.tick()

clock = ClockDisplay(15, 30)
clock.run()
