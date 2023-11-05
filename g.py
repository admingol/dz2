import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.grochi = 2500
    def to_study(self):
        print("Gabella")
        self.progress += 0.15
        self.gladness -= 3
    def spat(self):
        print("yraa")
        self.gladness += 5
    def work(self):
        print("babax")
        self.grochi += 150
        self.gladness -= 3
        self.progress += 0.1
    def shill(self):
        self.grochi -= 100
        self.gladness += 2
        self.progress -= 0.1
    def is_alive(self):
        if self.progress <- 0.5:
            print("smert vid tuposti")
            self.alive = False
        elif self.gladness <=0:
            print(":(")
            self.alive = False
        elif self.grochi <= 0:
            print("nema grochey")
        elif self.progress > 12:
            print("doctor nayk")
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
        print(f"Grochi = {self.grochi}")
    def live (self,day):
        day = "Day" + str(day) + "of" + self.name + "live"
        print(f"{day:^50}")
        vipadkove = random.randint(1,4)
        if vipadkove == 1:
            self.to_study()
        elif vipadkove == 2:
            self.spat()
        elif vipadkove == 3:
            self.shill()
        elif vipadkove == 4:
            self.work()
timofij = Student(name = "Timofij")

for day in range(365):
    if timofij.alive == False:
        break
    timofij.live(day)


