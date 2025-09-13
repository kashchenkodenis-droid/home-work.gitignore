class Pet:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.energy = 50

    def eat(self):
        self.energy += 10
        return f"{self.name} поїв."

    def play(self):
        self.energy -= 10
        return f"{self.name} пограв."

    def status(self):
        return f"{self.name} ({self.kind}), Energy={self.energy}"


class Cat(Pet):
    def speak(self): return "Мяу!"


class Dog(Pet):
    def speak(self): return "Гав!"


# Демонстрація
if __name__ == "__main__":
    cat = Cat("Мурчик", "cat")
    dog = Dog("Бобік", "dog")

    print(cat.speak(), cat.eat(), cat.status())
    print(dog.speak(), dog.play(), dog.status())
