from lab_python_oop.flying_object import FlyingObject

class Glider(FlyingObject):
    def __init__(self, name = "Планер", speed = 100.0):
        super().__init__(name, speed)

    def calculate_fuel(self, distance: float) -> float:
        if distance < 0:
            return "Расстояние не может быть отрицательным"
        return 0.0

    def calculate_time(self, distance: float) -> float:
        return super().calculate_time(distance)
    
