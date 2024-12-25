class StringVar:
    def __init__(self, value=""):
        self._value = value  # Инициализация строки с возможностью передать значение при создании объекта

    def set(self, value):
        """Метод для изменения содержимого строки."""
        self._value = value

    def get(self):
        """Метод для получения содержимого строки."""
        return self._value


# Создаем объект типа StringVar
string_var = StringVar("Initial string")

# Тестируем методы set() и get()
print("Initial value:", string_var.get())  # Выводим начальное значение

# Меняем содержимое строки
string_var.set("Updated string")
print("Updated value:", string_var.get())  # Выводим обновленное значение
