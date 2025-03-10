class Point:
    def __init__(self,x,y):
        self.x = x
        self.y =y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point(45,66)
# print(point1.y)
# point1.draw()

# constructors
class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


person1 = Person('steve')
# print(person1.name)


# inheritance

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")

class Cat(Mammal):
    pass


dog1 = Dog()
dog1.bark()