class Time:

    def __init__(self,hour,min,sec):
        self.hour = hour
        self.min = min
        self.sec = sec

    def _normalize(self):
        extra_mins = self.sec//60
        self.sec = self.sec%60
        self.min = self.min + extra_mins

        extra_hours = self.min//60
        self.min = self.min%60
        self.hour = self.hour+extra_hours

    def add_seconds(self,seconds):
        self.sec += seconds
        self._normalize()
        return self 
    
    def subtract_seconds(self,seconds):
        total_seconds = (self.hour*3600 + self.min*60 + self.sec) - seconds

        # we will handle the negative time by making it 00:00:00
        if(total_seconds<0):
            self.hour=0
            self.min=0
            self.sec=0
        else:
            self.hour = total_seconds//3600
            remaining = total_seconds%3600
            self.min = remaining//60
            self.sec = remaining%60
        
        return self 
    
    def __str__(self):
        return f" {self.hour:02d} : {self.min:02d} : {self.sec:02d} "
    
    @staticmethod

    def demonstrate():
        print(f"-"*20)
        print(f"Time class demonstrator !")
        print(f"-"*20)

        print("----")
        print("example 1")
        time1 = Time(2,39,58)
        print(f" The initial time :     {time1} ")

if __name__ == "__main__":
        Time.demonstrate()