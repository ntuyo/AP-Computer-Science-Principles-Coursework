class Time(object):
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __add__(self, other):
        self.hour += other.hour
        self.minute += other.minute
        self.second += other.second
        return self


time1 = Time(5, 32, 0)
time2 = Time(23, 11, 11)
total_time = time1 + time2
print(total_time.hour, ':', total_time.minute, ":", total_time.second)

