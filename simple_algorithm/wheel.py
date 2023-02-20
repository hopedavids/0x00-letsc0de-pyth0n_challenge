#!/usr/bin/python3

class Wheel():
    
    def __init__(self, name, position):
       self.name = name
       self.position = position

    def BMW_Car(self):
        print(f"This car has a wheel named {self.name} and is at the {self.position} position")
    
    def jeep(self):
        self.name = "jeep"
        print(f"This car has a wheel named {self.name} and is at the {self.position} position")
