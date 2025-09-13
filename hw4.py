from datetime import date

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_birthday_year(self):
        return date.today().year - self.age


class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

dog = Dog("Рекс", 3, "Вівчарка")
print(f"{dog.name} народився у {dog.get_birthday_year()} році")
