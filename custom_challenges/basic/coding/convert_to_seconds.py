"""
Task:

Write a program that will take the number of days, hours, minutes and seconds and 
return the total number of seconds
Assume that all data is valid

Challenge ID: fa45de6d1aaf0dcb
"""

def convert_to_seconds(days: int, hours: int, minutes: int, seconds: int) -> int:
    # Your code here
    return 0

######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

def run_test():
    import sys
    sys.path.append('..')
    from challenge_utils.unit_tests import UnitTest
    from challenge_utils.generate_id import generate_id
    test = UnitTest(generate_id(__file__))

    # Standard tests
    print(test.assert_equals(lambda: convert_to_seconds(0, 0, 1, 55), 115))
    print(test.assert_equals(lambda: convert_to_seconds(0, 0, 5, 25), 325))
    print(test.assert_equals(lambda: convert_to_seconds(0, 3, 1, 55), 10915))
    print(test.assert_equals(lambda: convert_to_seconds(0, 25, 0, 1), 90001))
    print(test.assert_equals(lambda: convert_to_seconds(0, 4, 3, 16), 14596))
    print(test.assert_equals(lambda: convert_to_seconds(3, 7, 2, 55), 284575))
    print(test.assert_equals(lambda: convert_to_seconds(30, 0, 5, 55), 2592355))
    print(test.assert_equals(lambda: convert_to_seconds(360, 10, 1, 55), 31140115))
    print(test.assert_equals(lambda: convert_to_seconds(364, 23, 59, 59), 31535999))

    # Random tests

if __name__ == "__main__":
    run_test()