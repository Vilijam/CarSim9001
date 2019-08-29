from random import randint

class Car(object):
    pass

class Wheel(object):

    def __init__(self):
        self.orientation = randint(1,360)

    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360

class Engine(object):

    def __init__(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()

    def updateModel(self, dt):
        if self.theTank.contents != 0:
            self.currentRpm =self.throttlePosition * self.maxRpm
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(self.currentRpm * (dt / 60))
        else:
            self.currentRpm = 0



    pass
class Gearbox(object):

    def __init__(self):
        self.wheels = {}
        self.currentGear = 0
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]

        listOWheels = ["frontLeft", "frontRight", "rearLeft", "rearRight"]
        for e in listOWheels:
            self.wheels[e] = Wheel()

    def shiftUp(self):
        if self.currentGear + 2 > len(self.gears) or self.clutchEngaged == True:
            pass
        else:
            self.currentGear += 1

    def shiftDown(self):
        if self.currentGear == 0 or self.clutchEngaged == True:
            pass
        else:
            self.currentGear -= 1

    def rotate(self, revolutions):
        if self.clutchEngaged != True:
            pass
        else:
            for e in self.wheels:
                self.wheels[e].rotate(revolutions * self.gears[self.currentGear])

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def refuel(self):
        self.contents = self.capacity

    def remove(self, amount):
        if self.contents - amount < 0:
            self.contents = 0
        else:
            self.contents = self.contents - amount
