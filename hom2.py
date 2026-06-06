class Student:
    def __init__(self, name):
        self.name = name
        self.money = 100
        self.energy = 100
        self.knowledge = 50

    def work(self):
        self.money += 50
        self.energy -= 30
        print(f"{self.name} працює і заробляє гроші.")

    def study(self):
        self.knowledge += 20
        self.energy -= 20
        print(f"{self.name} вчиться.")

    def rest(self):
        self.energy += 30
        self.money -= 10
        print(f"{self.name} відпочиває.")

    def status(self):
        print(f"💰 {self.money} | ⚡ {self.energy} | 📚 {self.knowledge}")

    def live_month(self):

        if self.money < 50:
            self.work()
        elif self.knowledge < 60:
            self.study()
        elif self.energy < 40:
            self.rest()
        else:
            self.rest()



student = Student("Олег")

for month in range(1, 13):
    print(f"\n📅 Місяць {month}")
    student.live_month()
    student.status()


    if student.money < 0:
        print("Студент не зміг прожити рік 😢")
        break

print("\nСимуляція завершена")