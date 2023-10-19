from car_class import Car

car1 = Car("Chevy", "Corvette", 2021, "red") # Instance of a class

print("Car:")
print(car1.make)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.wheels)

car1.drive()
car1.stop()