import unittest
from TemperatureConversion import TemperatureConversion


class TestTemperatureConversion(unittest.TestCase):
    def test_celsius_to_kelvin(self):
        self.assertEqual(TemperatureConversion.convert_celsius_to_kelvin(0), 273.15, "Should be 273.15")

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(TemperatureConversion.convert_celsius_to_fahrenheit(0), 32, "Should be 32")

    def test_kelvin_to_celsius(self):
        self.assertEqual(TemperatureConversion.convert_kelvin_to_celsius(0), -273.15, "Should be -273.15")

    def test_kelvin_to_fahrenheit(self):
        self.assertEqual(TemperatureConversion.convert_kelvin_to_fahrenheit(0), -459.67, "Should be -459.67")

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(TemperatureConversion.convert_fahrenheit_to_celsius(0), -17.78, "Should be -17.78")

    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(TemperatureConversion.convert_fahrenheit_to_kelvin(0), 255.37, "Should be 255.37")


if __name__ == '__main__':
    unittest.main()
