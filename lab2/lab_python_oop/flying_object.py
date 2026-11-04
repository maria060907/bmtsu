from abc import ABC, abstractmethod

class FlyingObject(ABC):
    def __init__ (self, name: str, speed: float):
        self.name = name
        self.speed = float(speed)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value =="":
            return ("Имя должно содержать в себе хотя бы какие-то символы")
        self.__name = value

    @property
    def speed(self) -> float:
        return self.__speed

    @speed.setter
    def speed(self, value: float):
        if value <= 0:
            return "Летательный объект не летит. Скорость должна быть больше 0."
        self.__speed = float(value)

    def calculate_time(self, distance: float) -> float:
        if distance <= 0:
            return "Расстояние не может быть отрицательным."
        return distance/self.__speed

    @abstractmethod
    def calculate_fuel(self, distance: float) -> float:
        pass

    def get_flight_status(self) -> str:
        return "аппарат выполняет полет в штатном режиме."

    def __str__(self) -> str:
        return (f"Летательный аппарат: {self.__name}, Скорость: {self.__speed} км/ч")
