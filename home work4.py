class Divider:
    def __init__(self, number):
        self.number = number

    def divide(self, x):
        try:
            result = self.number / x
            return result
        except ZeroDivisionError:
            return "Помилка: ділення на нуль"
        except TypeError:
            return "Помилка: введено не число"


a = Divider(100)
print(a.divide(10))   # 10.0
print(a.divide(0))    # Помилка: ділення на нуль
print(a.divide("hi")) # Помилка: введено не число
