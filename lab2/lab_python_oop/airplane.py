from lab_python_oop.flying_object import FlyingObject

class Airplane(FlyingObject):
    def __init__(self, name = "Самолет", speed = 900.0, fuel_consuption = 3.5):
        super().__init__(name, speed)
        self.__fuel_consuption = float(fuel_consuption)

    @property
    def fuel_consuption(self) -> float:
        return self.__fuel_consuption

    @fuel_consuption.setter
    def fuel_consuption(self, value: float):
        if value <= 0:
            return "Расход топлива должен быть положительным."
        self.__fuel_consuption = float(value)

    def calculate_time(self, distance: float) -> float:
        if distance <= 0:
            return "Расстояние не может быть отрицательным."
        base_time = super().calculate_time(distance)
        return base_time + 0.2

    def calculate_fuel(self, distance: float) -> float:
        if distance < 0:
            return "Расстояние не может быть отрицательным."
        return distance * self.__fuel_consuption

    def get_flight_status(self) -> str:
        return "Самолет следует заданному маршруту."

    def __str__(self) -> str:
        return(f"Самолет: {self.name}, Скорость: {self.speed} км/ч, Расход топлива: {self.fuel_consuption} л/км")
    
