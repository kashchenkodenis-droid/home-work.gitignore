class Human:
    def __init__(self, name):
        self.name = name
        self.car = None

    def buy_car(self, car):
        self.car = car
        print(f"{self.name} купив {car.model}")

class Auto:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"{self.model} їде")

h = Human("Денис")
a = Auto("Tesla")
h.buy_car(a)
a.drive()
