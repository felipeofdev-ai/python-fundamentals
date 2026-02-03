# Basic Object-Oriented Programming example

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"My name is {self.name} and I am {self.age} years old."

person = Person("Felipe", 30)
print(person.introduce())
