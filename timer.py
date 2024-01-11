import time

class ClockDisplay:
    def __init__(self, hour_value, minute_value):
        self.hour = NumberDisplay(hour_value)
        self.minute = NumberDisplay(minute_value)

    def count_time(self):
        self.minute.tick() 
        if self.minute.v == 0:  
            self.hour.tick()

    def display_time(self):
        return f"{self.hour.v:02d}:{self.minute.v:02d}" 

class NumberDisplay:
    def __init__(self, init_value):
        self.v = init_value

    def tick(self):
        self.v = (self.v + 1) % 60 

class AmPmClockDisplay(ClockDisplay):
    def __init__(self, hour_value, minute_value):
        super().__init__(hour_value, minute_value)
        self.am_pm = "AM"

    def count_time(self):
        super().count_time()
        self.toggle_am_pm_if_needed()

    def toggle_am_pm_if_needed(self):
        if self.hour.v == 12 and self.minute.v == 00:
            self.am_pm = "AM" if self.am_pm == "PM" else "PM" 
        if self.hour.v == 13 and self.minute.v == 00:
            self.hour.v == 1

    def display_time(self):
        return f"{self.hour.v:02d}:{self.minute.v:02d} {self.am_pm}"
    

if __name__ == '__main__':
    clock = AmPmClockDisplay(12, 50) 
    while True:
        print(clock.display_time(), end='\r')
        clock.count_time()
        time.sleep(1)
