from car_class import Car

class Animal:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def what_kind_of_animal(self):
        print(f"Hello! My name is {self.name} and I'm a {self.animal}.")


class Breed(Animal):
    def __init__(self, animal, name, breed, length, weight):
        self.breed = breed
        self.length = length
        self.weight = weight

        Animal.__init__(self, animal, name)
    

animal_1 = Breed("Dog", "Pewee", "Chihuahua", 25, 1.7)
#animal_2 = Animal("Cat", "Bell")

animal_1.what_kind_of_animal()
print(animal_1)
#animal_2.what_kind_of_animal()