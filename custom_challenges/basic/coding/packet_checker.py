"""
Task:

Given a packet of data as input (refer to your notes if you're unsure!), 
check if the data has been corrupted using the parity system. Return True if
the data is corrupted, and False if it is not. Maximum size of 1 data packet is 32 bits

Examples:
packet_checker('10010010', "Even") -> True
packet_checker('10010011', "Even") -> False
packet_checker('10010010', "Odd") -> False
packet_checker('10010011', "Odd") -> True

packet_checker('000011010110111101101001', "Odd") -> False

Challenge ID: 9aa6d22f8f82c6f0
"""

def packet_checker(data_packet: str, parity_system: str) -> bool:
    # Your code here
    return False

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

    # Edge cases
    print(test.assert_equals(lambda: packet_checker('00000000', "Even"), False))
    print(test.assert_equals(lambda: packet_checker('11111101', "Odd"), False))
    print(test.assert_equals(lambda: packet_checker('10010101', "Odd"), True))
    print(test.assert_equals(lambda: packet_checker('10000101', "Even"), True))
    print(test.assert_equals(lambda: packet_checker('0000000', "Even"), True))
    print(test.assert_equals(lambda: packet_checker('', "Even"), True))

    # Standard tests
    print(test.assert_equals(lambda: packet_checker('10010010', "Even"), True))
    print(test.assert_equals(lambda: packet_checker('10010011', "Even"), False))
    print(test.assert_equals(lambda: packet_checker('10010010', "Odd"), False))
    print(test.assert_equals(lambda: packet_checker('10010011', "Odd"), True))
    print(test.assert_equals(lambda: packet_checker('00011000', "Even"), False))
    print(test.assert_equals(lambda: packet_checker('100010101011010101010011', "Even"), False))
    print(test.assert_equals(lambda: packet_checker('000011010110111101101001', "Odd"), False))

    # Random tests

if __name__ == "__main__":
    run_test()