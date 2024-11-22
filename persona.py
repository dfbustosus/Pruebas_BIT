import logging

class Person:
    def __init__(self, name: str, phone: str, email: str, surname: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.surname = surname

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"
    
    def __call__(self):
        pass