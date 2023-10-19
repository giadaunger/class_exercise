class Car:

    wheels = 4 # Class variable

    def __init__(self, make, model, year, color) -> None:
        self.make = make     # Instance of a variable
        self.model = model   # Instance of a variable
        self.year = year     # Instance of a variable
        self.color = color   # Instance of a variable

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car has stopped")