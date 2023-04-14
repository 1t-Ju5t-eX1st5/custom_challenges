"""
Task:
Given a list of values, return the largest number in the list
If no valid values are found, return False
Challenge notes: Using the min() or max() function is considered cheating
Return False as well if there are any non-numeric characters in the list

Challenge ID: 7d9e9d94e3764862
"""

def find_largest_number(lst: list) -> int | float | bool:
    if len(lst) < 1:
        return False
    filtered_list = []
    for char in lst:
        if type(char) == int or str(char).isnumeric():
            filtered_list.append(int(char))
        else:
            pass
    if len(filtered_list) < len(lst):
        return False
    largest_num = filtered_list[0]
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
    test = UnitTest(generate_id(__file__))

    # Edge tests
    print(test.assert_equals(lambda: find_largest_number([]), False))
    print(test.assert_equals(lambda: find_largest_number([1, 100, 100000]), 100000))
    print(test.assert_equals(lambda: find_largest_number([-1, -100, -100000]), -1))
    print(test.assert_equals(lambda: find_largest_number([0, 0, 0]), False))

    # Runtime tests
    print(test.assert_equals(lambda: find_largest_number([100, 125, 123, 524, 923]), 923))
    print(test.assert_equals(lambda: find_largest_number([72, 35, 50, 5, 66, 3, 45, 79, 27, 74, 91, 44, 65, 28, 92, 65, 43, 34, 65, 12, 25, 90, 20, 51, 45, 3, 23, 34, 78, 69, 66, 25, 72, 56, 94]), 94))
    print(test.assert_equals(lambda: find_largest_number([7, 6, 55, 47, 29, 58, 81, 19, 58, 65, 48, 2, 72, 72, 10, 52, 20, 17, 98, 27, 41, 63, 31, 12, 100, 55, 61, 75, 100, 9, 54, 26, 37, 99, 72]), 100))
    print(test.assert_equals(lambda: find_largest_number([160, 62, 241, 37, 120, 217, 186, 103, 184, 202, 141, 174, 248, 231, 13, 172, 95, 21, 6, 199, 21, 164, 177, 215, 144, 152, 200, 25, 33, 162, 103, 107, 244, 34, 168, 181, 72, 200, 110, 144, 37, 247, 197, 215, 140, 52, 89, 54, 180, 159]), 248))
    print(test.assert_equals(lambda: find_largest_number([176, 168, 45, 98, 183, 155, 163, 106, 109, 138, 175, 40, 135, 164, 41, 124, 131, 147, 187, 215, 117, 213, 129, 15, 177, 116, 246, 182, 100, 171, 96, 154, 52, 167, 120, 75, 19, 94, 93, 64, 177, 170, 163, 126, 186, 62, 215, 195, 83, 53]), 246))

    # Invalid input data tests
    print(test.assert_equals(lambda: find_largest_number(['A']), False))
    print(test.assert_equals(lambda: find_largest_number(['What', 'Is', 'This', 'Input']), False))
    print(test.assert_equals(lambda: find_largest_number(['What', 'is', 6, 'times', 9]), False))
    print(test.assert_equals(lambda: find_largest_number(['5', '7', '9', '11']), 11))    # Sike. This is a valid data set :P
    print(test.assert_equals(lambda: find_largest_number([False, True, False, False, True]), False))


if __name__ == "__main__":
    run_test()