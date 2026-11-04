import unittest
from lab_python_oop.glider import Glider
from lab_python_oop.airplane import Airplane
from lab_python_oop.rocket import Rocket

class TestFlyingObjects(unittest.TestCase):

    def test_glider(self):
        glider = Glider("Спортивный планер «АС-4»", 150.0)
        self.assertEqual(glider.name, "Спортивный планер «АС-4»")
        self.assertEqual(glider.speed, 150.0)
        self.assertEqual(glider.calculate_time(300.0), 2.0)
        self.assertEqual(glider.calculate_fuel(300.0), 0.0)

    def test_airplane(self):
        plane = Airplane("Пассажирский Airbus A320", 800.0, 4.0)
        self.assertEqual(plane.name, "Пассажирский Airbus A320")
        self.assertEqual(plane.speed, 800.0)
        self.assertEqual(plane.fuel_consuption, 4.0)
        self.assertAlmostEqual(plane.calculate_time(800.0), 1.2)
        self.assertEqual(plane.calculate_fuel(100.0), 400.0)

    def test_rocket(self):
        rocket = Rocket("Ракета-носитель «Falcon 1»", 12000.0, 50.0)
        self.assertEqual(rocket.name, "Ракета-носитель «Falcon 1»")
        self.assertEqual(rocket.speed, 12000.0)
        self.assertEqual(rocket.fuel_consumption, 50.0)
        self.assertEqual(rocket.calculate_fuel(200.0), 10000.0)

if __name__ == "__main__":
    unittest.main()
