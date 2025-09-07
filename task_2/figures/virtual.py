from abc import ABC, abstractmethod


# Создадим виртуальный класс и определим в нем методы, это будет нашим интерфейсом для пользователей
class Figure(ABC):

    # Функция нахождения площади
    @abstractmethod
    def square(self) -> int | float:
        pass
