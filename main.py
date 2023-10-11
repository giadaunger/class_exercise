class Animal:
    def __init__(self, animal, breed, name):
        self.animal = animal
        self.breed = breed
        self.name = name

    def what_kind_of_animal(self):
        print(f"Hello! My name is {self.name} and I'm a {self.animal}, my breed is {self.breed}")
    

animal_1 = Animal("Dog", "chihuahua", "Pewee")
animal_1.what_kind_of_animal()