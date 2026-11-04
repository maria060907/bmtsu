from colorama import Fore, Style, init
from lab_python_oop.airplane import Airplane
from lab_python_oop.glider import Glider
from lab_python_oop.rocket import Rocket

def main():
  print("1 - Запуск программы;\n")
  print("0 - Выйти из программы.\n")
  choice1 = input("Введите число (1, 0): ")

  while choice1 != 0:
    print("=== СИСТЕМА УПРАВЛЕНИЯ ЛЕТАТЕЛЬНЫМИ АППАРАТАМИ ===\n")

    print("Выберите тип объекта для демонстрации:")
    print("1. Планер")
    print("2. Самолет")
    print("3. Ракета")

    choice = input("Введите номер пункта (1-3): ").strip()

    obj = None
    if choice == "1":
      obj = Glider("Спортивный планер «АС-4»", 150.0)
    elif choice == "2":
      obj = Airplane("Пассажирский Airbus A320", 820.0, 3.8)
    elif choice == "3":
      obj = Rocket("Ракета-носитель «Falcon 1»", 14000.0, 85.0)
    else:
      print("Неверный выбор.")

    print("\n--- Демонстрация вывода через print (метод __str__) ---")
    print(obj)

    print("\n--- Проверка свойств (геттеры и сеттеры) ---")
    print(f"Текущая скорость: {obj.speed} км/ч")

    print("Введите дистанцию:")
    distance = int(input())
    print(f"\n--- Расчеты для расстояния {distance} км ---")
    print(f"Время в пути: {obj.calculate_time(distance):.2f} ч")
    print(f"Требуемое топливо: {obj.calculate_fuel(distance)}")
    print(f"Статус полета: {obj.get_flight_status()}")

if __name__ == "__main__":
  main()
