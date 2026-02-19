class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):          # overrides Animal.speak
        print("The dog barks")

d = Dog()
d.speak()   # -> The dog barks
