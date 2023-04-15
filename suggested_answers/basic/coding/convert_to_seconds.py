"""
Task:

Write a program that will take the number of days, hours, minutes and seconds and 
return the total number of seconds
Assume that all data is valid

Challenge ID: fa45de6d1aaf0dcb
"""

def convert_to_seconds(days: int, hours: int, minutes: int, seconds: int) -> int:
    return (days * 86400) + (hours * 3600) + (minutes * 60) + seconds

######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

import unittest
class Test_SecondsConversion(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(convert_to_seconds(0, 0, 0, 50), 50)
        self.assertEqual(convert_to_seconds(0, 0, 5, 0), 300)
        self.assertEqual(convert_to_seconds(0, 3, 0, 0), 10800)
        self.assertEqual(convert_to_seconds(1, 0, 0, 0), 86400)
    
    def test_full_cases(self):
        self.assertEqual(convert_to_seconds(0, 0, 1, 55), 115)
        self.assertEqual(convert_to_seconds(0, 3, 1, 55), 10915)
        self.assertEqual(convert_to_seconds(0, 25, 0, 1), 90001)
        self.assertEqual(convert_to_seconds(3, 7, 2, 55), 284575)
        self.assertEqual(convert_to_seconds(30, 0, 5, 55), 2592355)
        self.assertEqual(convert_to_seconds(360, 10, 1, 55), 31140115)
        self.assertEqual(convert_to_seconds(364, 23, 59, 59), 31535999)

if __name__ == "__main__":
    unittest.main()