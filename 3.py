class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    def greet(self):
        return "hello student", self.first_name


class Student(Person):
    def is_student(self):
        return True


a = Student("Nazar")
print(a.greet())
print(a.is_student())
