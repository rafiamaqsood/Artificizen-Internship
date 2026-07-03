# Add a @classmethod to a Person class that works as an alternate constructor, e.g. Person.from_birth_year(name, year).

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    @classmethod
    def from_birth_year(cls, name, birthyear):
        age= 2026-birthyear
        return cls(name,age)

person= Person("Rafia", 20)
print(person.name, person.age)
person2=Person.from_birth_year("Sawera", 1992)
print(person2.name, person2.age)