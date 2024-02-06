from enum import Enum

Gender = Enum('Gender', ['Male', 'Female', 'Other'])

class Patient:
    def __init__(self, name: str, age: int, gender: Gender, contact_number: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact_number = contact_number

    def __repr__(self):
        return f"Patient({self.name!r}, age={self.age!r}, gender={self.gender.name!r}, contact_number={self.contact_number!r})"
    
    def __rich_repr__(self):
        yield self.name
        yield "age", self.age
        yield "gender", self.gender.name
        yield "contact_number", self.contact_number