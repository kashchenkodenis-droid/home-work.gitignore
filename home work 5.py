class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


def wrapper(func, *args):
    try:
        result = func(*args)
        return result
    except Exception as e:
        return f"Сталася помилка: {e}"


# приклади використання
print(wrapper(Calculator.add, 5, 3))
print(wrapper(Calculator.multiply, 4, 7))
print(wrapper(Calculator.add, "5", 3))
