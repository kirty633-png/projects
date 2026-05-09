class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Driver(Person):
    def __init__(self, name, age, driving_licence):
        super().__init__(name, age)
        self.driving_licence = driving_licence

name = input('name')
age = input('age')
dl = input('driving_licence')



driver = Driver(name, age, dl)