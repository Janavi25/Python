class Animals:
    def walk(self):
        print("walk")


class Cat(Animals):
    pass


class Dog(Animals):
    def bark(self):
        print("dog is barking")


dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
