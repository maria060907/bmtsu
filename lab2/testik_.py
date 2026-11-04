import unittest
from lab_python_oop.glider import Glider
from lab_python_oop.airplane import Airplane
from lab_python_oop.rocket import Rocket

class TestFlyingObjects(unittest.TestCase):

    def test_glider(self):
        """Тестирование планера"""
        glider = Glider("Спортивный планер", 150.0)
        self.assertEqual(glider.name, "Спортивный планер")
        self.assertEqual(glider.speed, 150.0)
        self.assertEqual(glider.calculate_time(300.0), 2.0)
        self.assertEqual(glider.calculate_fuel(300.0), 0.0)

    def test_airplane(self):
        """Тестирование самолета"""
        plane = Airplane("Airbus", 800.0, 4.0)
        self.assertEqual(plane.name, "Airbus")
        self.assertEqual(plane.speed, 800.0)
        self.assertEqual(plane.fuel_consuption, 4.0)
        self.assertAlmostEqual(plane.calculate_time(800.0), 1.2)
        self.assertEqual(plane.calculate_fuel(100.0), 400.0)

    def test_rocket(self):
        """Тестирование ракеты"""
        rocket = Rocket("Falcon", 12000.0, 50.0)
        self.assertEqual(rocket.name, "Falcon")
        self.assertEqual(rocket.speed, 12000.0)
        self.assertEqual(rocket.fuel_consumption, 50.0)
        self.assertEqual(rocket.calculate_fuel(200.0), 10000.0)

if __name__ == "__main__":
    unittest.main()
