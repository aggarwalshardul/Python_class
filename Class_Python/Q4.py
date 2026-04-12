class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print("Dog barks")

d = Dog()

d.speak()  # inherited from Animal
d.bark()   # from Dog class