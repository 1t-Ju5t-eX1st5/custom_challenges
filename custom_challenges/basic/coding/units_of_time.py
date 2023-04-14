"""
Write a function that will convert the number of seconds into a 
human-readable format, and return it

Assume that all inputs are valid

Format:
"x years, x days, x hours, x minutes and x seconds"

Challenge references:
1 minute -> 60 seconds
1 hour -> 3600 seconds
1 day -> 86400 seconds
1 year -> 31536000 seconds
"""

def units_of_time(seconds: int) -> str:
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
    test = UnitTest()
    CHALLENGE_ID = generate_id(__file__)

    # Standard tests
    print(test.assert_equals(lambda: units_of_time(53), "53 seconds"))
    print(test.assert_equals(lambda: units_of_time(300), "5 minutes"))
    print(test.assert_equals(lambda: units_of_time(325), "5 minutes and 25 seconds"))
    print(test.assert_equals(lambda: units_of_time(3610), "1 hour and 10 seconds"))
    print(test.assert_equals(lambda: units_of_time(86410), "1 day and 10 seconds"))
    print(test.assert_equals(lambda: units_of_time(432060), "5 days and 1 minute"))
    print(test.assert_equals(lambda: units_of_time(31536000), "1 year"))
    print(test.assert_equals(lambda: units_of_time(567648000), "18 years"))
    print(test.assert_equals(lambda: units_of_time(31535999), "1 year, 364 days, 23 hours, 59 minutes and 59 seconds"))

    # Random tests

if __name__ == "__main__":
    run_test()