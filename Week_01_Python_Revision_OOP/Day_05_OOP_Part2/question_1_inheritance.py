# Create a base class Animal with a speak() method, and Dog/Cat subclasses that override it. 
class Animal:
    def speak(self, sound):
        self.sound = sound
        print(f"Animals have unique voices like this say {self.sound}")

class Cat(Animal):
    def speak(self, sound):
        self.sound = sound
        print(f"Cat says {self.sound}")
class Dog(Animal):
    def speak(self, sound):
        self.sound = sound
        print(f"Dog says {self.sound}")

cat =Cat()
cat.speak("meow")
dog = Dog()
dog.speak("bark")