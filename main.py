# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def get_area(self):
#         return pi * self.radius * self.radius
#
#
# circle1 = Circle(10)
# print(circle1.get_area())


# class Calculator:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return f'{self.a} + {self.b} = {self.a + self.b}'
#
#     def subtract(self):
#         return f'{self.a} - {self.b} = {self.a - self.b}'
#
#     def multiply(self):
#         return f'{self.a} * {self.b} = {self.a * self.b}'
#
#     def divide(self):
#         return f'{self.a} / {self.b} = {self.a / self.b}'
#
# calc1 = Calculator(1, 2)
# print(calc1.add())
# print(calc1.multiply())
# print(calc1.divide())
# print(calc1.subtract())


# class Employee:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#
#     @property
#     def fullname(self):
#         return f'{self.first_name} {self.last_name}'
#
#     @property
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@iitu.edu"
#
# employee1 = Employee('Dilyara', 'Daniyarkyzy')
# print(employee1.fullname)
# print(employee1.email)



# def get_student_names(student_names: dict) -> list:
#     return list(student_names.values())
#
# student_names = {
#     "Student 1" : "Steve",
#     "Student 2" : "Becky",
#     "Student 3" : "John",
# }
#
# result = get_student_names(student_names)
# print(result)


import  re

def is_valid(text):
    if re.match(r' ', text):
        return True
    return False

print(is_valid())


# import re
# def letters_only(text):
#     return re.sub(r'YOUR REGEX CODE', '', text)




























