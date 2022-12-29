class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")
class Pickup(Vehicle):
    pass;
class Car(Vehicle):
    pass;
class Van(Vehicle):
    pass;
class Estate(Vehicle):
    pass;

pickup1 = Pickup()
pickup1.turnOnAirConditioner()

car1 = Car()
car1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estate1 = Estate()
estate1.turnOnAirConditioner()