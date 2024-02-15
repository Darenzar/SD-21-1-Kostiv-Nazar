class Person:
    def __init__(self, first_name):
        self.first_name = first_name
    def greet(self):
        print("helo student")


class Student(Person):
    pass


a = Person("Nazar")
