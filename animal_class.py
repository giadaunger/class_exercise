class Animal:
    
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Fish(Animal):
    def swim(self):
        print("This fish is swimming")

class Bird(Animal):
    def fly(self):
        print("This bird is flying")

class Rabbit(Animal):
    def run(self):
        print("This rabbit is running")



fish = Fish()
bird = Bird()
rabbit = Rabbit()