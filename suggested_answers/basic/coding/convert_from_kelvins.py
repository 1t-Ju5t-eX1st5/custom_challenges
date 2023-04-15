"""
Task:

Given a temperature (in Kelvins) and the temperature unit to convert to, write
a function that will return the converted temperature rounded to 2
decimal places. Assume that all values provided are valid

Formula References:
Kelvins to Celsius: K - 273.15
Kelvins to Fahrenheit: (K − 273.15) × 9/5 + 32

Challenge ID: da53908e0517cd63
"""

def convert_temperature(temperature_kelvins: int | float, to_convert: str) -> int | float:
    return round((temperature_kelvins - 273.15), 2) if to_convert == "C" else round(((temperature_kelvins - 273.15) * 9 / 5) + 32, 2)



######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

import unittest
class Test_TemperatureConvert(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(convert_temperature(0, "F"), -459.67)
        self.assertEqual(convert_temperature(0, "C"), -273.15)
    
    def test_fahrenheit_conversion(self):
        self.assertEqual(convert_temperature(150, "F"), -189.67)
        self.assertEqual(convert_temperature(300, "F"), 80.33)
        self.assertEqual(convert_temperature(5000, "F"), 8540.33)
        self.assertEqual(convert_temperature(1e10, "F"), 17999999540.33)
    
    def test_celsius_conversion(self):
        self.assertEqual(convert_temperature(150, "C"), -123.15)
        self.assertEqual(convert_temperature(300, "C"), 26.85)
        self.assertEqual(convert_temperature(5000, "C"), 4726.85)
        self.assertEqual(convert_temperature(1e10, "C"), 9999999726.85)

if __name__ == "__main__":
    unittest.main()