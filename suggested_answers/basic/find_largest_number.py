"""
Task:
Given a list of values, return the largest number in the list
If no valid values are found, return False
Challenge notes: Using the min() or max() function is considered cheating
Return False as well if there are any non-numeric characters in the list

Challenge ID: 7d9e9d94e3764862
"""

def find_largest_number(lst: list) -> int | float | bool:
    filtered_list = []
    for char in lst:
        if str(char).isnumeric():
            filtered_list.append(int(char))
        else:
            pass
    if len(filtered_list) < len(lst):
        return False
    largest_num = 0
    for num in lst:
        if int(num) > largest_num:
            largest_num = int(num)
    return largest_num

######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

def run_test():
    import sys
    sys.path.append('..')
    from challenge_utils.generate_id import generate_id
    from challenge_utils.unit_tests import UnitTest
    test = UnitTest()
    CHALLENGE_ID = generate_id(__file__)

    # Standard tests
    print(test.assert_equals(lambda: find_largest_number([0, 1, 3, 5]), 5))
    print(test.assert_equals(lambda: find_largest_number([1, 1, 7, 2, 5, 9]), 9))
    print(test.assert_equals(lambda: find_largest_number([0, 0]), 0))
    print(test.assert_equals(lambda: find_largest_number([100, 125, 123, 524, 923]), 923))
    print(test.assert_equals(lambda: find_largest_number([300, 323, 194, 231]), 323))

    # Invalid input data tests
    print(test.assert_equals(lambda: find_largest_number(['A']), False))
    print(test.assert_equals(lambda: find_largest_number(['What', 'Is', 'This', 'Input']), False))
    print(test.assert_equals(lambda: find_largest_number(['What', 'is', 6, 'times', 9]), False))
    print(test.assert_equals(lambda: find_largest_number(['5', '7', '9', '11']), 11))    # Sike. This is a valid data set :P
    print(test.assert_equals(lambda: find_largest_number([False, True, False, False, True]), False))

    # Random tests

if __name__ == "__main__":
    run_test()