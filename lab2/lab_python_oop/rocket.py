from lab_python_oop.flying_object import FlyingObject


class Rocket(FlyingObject):

  def __init__(self, name: str = "Космическая ракета", speed: float = 11000.0, fuel_consumption: float = 60.0,):
    super().__init__(name, speed)
    self.__fuel_consumption = float(fuel_consumption)

  @property
  def fuel_consumption(self) -> float:
    return self.__fuel_consumption

  @fuel_consumption.setter
  def fuel_consumption(self, value: float):
    if value <= 0:
      raise ValueError("Расход топлива ракеты должен быть положительным.")
    self.__fuel_consumption = float(value)

  def calculate_fuel(self, distance: float) -> float:
    if distance < 0:
      return "Расстояние не может быть отрицательным."
    return distance * self.__fuel_consumption

  def __str__(self) -> str:
    return (f"Ракета: «{self.name}», Скорость: {self.speed} км/ч, Расход топлива:{self.__fuel_consumption} кг/км")
