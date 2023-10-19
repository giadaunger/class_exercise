class Car:

    """
        Class varibles are declared inside the class bt outside of the cunstructor
        and you can set a default value for all class instances.
        Although the class variable has e default value, you can change it later on
    """
    wheels = 4 # Class variable

    def __init__(self, make, model, year, color) -> None:
        """
            Instance of variables are declared inside cunstructor (the dunder init 
            method) and can be given unique values 
        """ 
        self.make = make     # Instance of a variable
        self.model = model   # Instance of a variable
        self.year = year     # Instance of a variable
        self.color = color   # Instance of a variable

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car has stopped")