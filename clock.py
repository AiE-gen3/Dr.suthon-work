import time

class Clock:
    def __init__(self, hour, minute) -> None:
        self.hour = hour
        self.minute = minute
        self.second = 0

class MinuteClock(Clock):
    def __init__(self, hour, minute) -> None:
        super().__init__(hour, minute)

    def set_minute(self, minute):
        self.minute = minute

    def get_minute(self):
        return self.minute

    def count_time(self):
        self.minute += 1  # Increment seconds first
        #if self.second == 60:
         #   self.minute += 1
          #  self.second = 0
        if self.minute == 60:
            self.hour += 1
            self.minute = 0
        if self.hour == 24:
            self.hour = 0

if __name__ == '__main__':
    clock = MinuteClock(23, 49)
    while True:
        print(f'{clock.hour:02d}:{clock.minute:02d}', end='\r')  # Format for 2 digits
        clock.count_time()
        time.sleep(1)
