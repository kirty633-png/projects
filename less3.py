class Human:
    def __init__(self, name):
        self.name = name


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []
        self.driver = None

    def add_passenger(self, human: Human, is_driver:bool):
        self.passengers.append(human)
        if is_driver:
            self.driver = human

    def driver(self):
        if self.driver is None:
            print(f'Car cannot drive without driver.')
        else:
            print(f'Car {self.driver} is driving.')


    def show_passengers(self):
        print(f'in {self.brand} there is (are):')
        for passenger in self.passengers:
            print(passenger.name)

        if self.driver is not None:
            print(f'Driver: {self.driver.name}')



kiril = Human("Kiril")
mark = Human("Mark")

bmw =  Car("BMW M5 f90")
bmw.add_passenger(kiril, False)
# bmw.add_passenger(mark, True)

bmw.show_passengers()
bmw.driver()