from random import randint

class Car(object):

    def __init__(self):
        self.theEngine = Engine()

    def updateModel(self, dt):
        self.theEngine.updateModel(dt)
        #Metode til at aktivere en anden metode???? Jeg gætter på det gør programmet mere ordenligt

class Wheel(object):

    def __init__(self):
        self.orientation = randint(0,360)
        #Hjulet bliver tildelt en tilfældig orientation

    def rotate(self, revolutions):
        self.orientation = (self.orientation + (revolutions * 360)) % 360
        #Hjulet bliver drejet udfra revolutions fra Gearbox. Matematikken sikre at orientationen forbliver mellem 0 og 360.

class Engine(object):

    def __init__(self):
        self.throttlePosition = 0
        self.theGearbox = Gearbox()
        self.currentRpm = 0
        self.consumptionConstant = 0.0025
        self.maxRpm = 100
        self.theTank = Tank()
        #deklarer variabler


    def updateModel(self, dt):
        #"bruger" brændstof, hvis der er noget. Drejer hjul og fjerner brændstof
        if self.theTank.contents != 0:
            self.currentRpm = self.throttlePosition * self.maxRpm
            self.theTank.remove(self.currentRpm * self.consumptionConstant)
            self.theGearbox.rotate(self.currentRpm * (dt / 60))
        else:
            self.currentRpm = 0

class Gearbox(object):

    def __init__(self):
        self.wheels = {}
        self.currentGear = 0
        self.clutchEngaged = False
        self.gears = [0, 0.8, 1, 1.4, 2.2, 3.8]
        #nuværende gear, kobling og koblingskoefficienter bliver deklareret


        listOWheels = ["frontLeft", "frontRight", "rearLeft", "rearRight"]
        for e in listOWheels:
            self.wheels[e] = Wheel()

            #Hvorfor deklarede jeg hjulene på denne måde? idfk, jeg er dum, tror jeg.
            #Jeg gad ikke skrive xxx = Wheel() fire gange, så jeg gjorde det sådan.

    def shiftUp(self):
        if self.currentGear < len(self.gears) -1 and self.clutchEngaged == False:
            #tjekker om der er et højere gear
            self.currentGear += 1

    def shiftDown(self):
        if self.currentGear > 0 and self.clutchEngaged == False:
            #den kan ikke gå ned i gear, hvis den allerede er i bakgear
            self.currentGear -= 1

    def rotate(self, revolutions):
        if self.clutchEngaged == False:
            #tjekker om koblingen er løftet
            pass
        else:
            for e in self.wheels:
                self.wheels[e].rotate(revolutions * self.gears[self.currentGear])
                #for hvert element i wheels=dictionariet roteres et hjul

class Tank(object):

    def __init__(self):
        self.capacity = 100
        self.contents = 100
        #deklarer tankens maksimale kapasitet og nuværende last.

    def refuel(self):
        self.contents = self.capacity
        #metode til at tanke op. nuværende last bliver lig maks

    def remove(self, amount):
        if self.contents - amount < 0:
        #tjekke om der bliver forsøgt at bruge mere brændstof end der er i tanken.
            self.contents = 0
        else:
            self.contents = self.contents - amount
            #hvis der bliver fjernet =< brændstof end der er i tanken, bliver det fjernet
