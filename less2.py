import random
from random import choice

class Student:
    def __init__(self, name: str):
        self.name = name
        self.skills = random.randint(1, 5)
        self.money = random.randint(50, 100)

    def introduce(self):
        print(f'My name is {self.name}.')
        print(f'My skills is {self.skills}.')
        print(f'I have {self.money}$')

    def study(self):
        print('Time to study.')
        self.skills += 1

    def chill(self):
        print('Time to chill.')
        self.skills -= 0.3
        costs = random.randint(100, 200)
        self.money -= costs
        print(f'-  {costs}$')

    def work(self):
        print('Time to work.')
        income = random.randint(100, 500)
        self.money += income
        self.skills += 0.5
        print(f'+ {income}$')



student = Student("kiril")
student.introduce()


for day in range(1, 366):
    print(f'Day - {day}')

    choice = random.randint(0, 2)

    if choice == 0:
        student.study()
    elif choice == 1:
        student.work()
    else:
        student.chill()

    print("============")
student.introduce()
