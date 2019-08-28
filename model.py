from random import randint

class Car(object):
    pass

class Wheel(object):

    def __init__(self):
        self.orientation = randint(1,360)

    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360

class Engine(object):
    pass

class Gearbox(object):

    def __init__(self):
        self.wheels = {}
        self.currentGear = 0
        self.clutchEngaged = False
        self.gears [0, 0.8, 1, 1.4, 2.2, 3.8]

        listOWheels = ["frontLeft", "frontRight", "rearLeft", "rearRight"]
        for e in listOWheels:
            self.wheels[e] = Wheel()

    def shiftUp(self):
        pass

    def shiftDown(self):
        pass

    def rotate(self, revolutions):
        pass

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100

    def refuel(self):
        self.contents = self.capacity

    def remove(self, amount):
        if(self.contents - amount < 0):
            self.contents = 0
        else:
            self.contents = self.contents - amount
