"""
Given a number n, write a program that generates and returns the Fibonacci sequence up
to that number in a list format. 

The Fiboacci sequence is a series of numbers in which each number is the sum of the two 
previous ones. An example of the Fibonacci sequence where n = 7 is

fibonacci_sequence(7) -> [0, 1, 1, 2, 3, 5, 8, 13]

Challenge notes:
n can appear in both string and integer format, so remember to convert the variable type
as and when its required

Challenge ID: df13ea19e9651342
"""

def fibonacci_sequence(n: int | str) -> list:
    # Your code here
    return []


######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

import unittest
class Test_FibonacciSequence(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci_sequence(0), [])
        self.assertEqual(fibonacci_sequence("1"), [0])
    
    def test_full_cases(self):
        self.assertEqual(fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])
        self.assertEqual(fibonacci_sequence(15), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])
        self.assertEqual(fibonacci_sequence(20), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])
        self.assertEqual(fibonacci_sequence("20"), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711])
        self.assertEqual(fibonacci_sequence(30), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229])
        self.assertEqual(fibonacci_sequence("30"), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229])

    def test_invalid_cases(self):
        # Not applicable for this challenge
        return 0

if __name__ == "__main__":
    unittest.main()