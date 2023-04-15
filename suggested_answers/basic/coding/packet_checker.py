"""
Task:

Given a packet of data as input (refer to your notes if you're unsure!), 
check if the data has been corrupted using the parity system. Return True if
the data is corrupted, and False if it is not. Maximum size of 1 data packet is 32 bits
Return True for invalid data (data length is not multiple of 8, empty string)

Examples:
packet_checker('10010010', "Even") -> True
packet_checker('10010011', "Even") -> False
packet_checker('10010010', "Odd") -> False
packet_checker('10010011', "Odd") -> True

packet_checker('000011010110111101101001', "Odd") -> False

Challenge ID: 9aa6d22f8f82c6f0
"""

def packet_checker(data_packet: str, parity_system: str) -> bool:
    if len(data_packet) < 1 or len(data_packet) % 8 != 0:
        return True
    if parity_system == "Even":
        if data_packet.count('1') % 2 == 0:
            return False
        else:
            return True
    else:
        if data_packet.count('1') % 2 == 1:
            return False
        else:
            return True

######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

import unittest
class Test_PacketChecker(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(packet_checker('00000000', "Even"), False)
        self.assertEqual(packet_checker('11111101', "Odd"), False)
        self.assertEqual(packet_checker('10010101', "Odd"), True)
        self.assertEqual(packet_checker('10000101', "Even"), True)
        self.assertEqual(packet_checker('0000000', "Even"), True)
        self.assertEqual(packet_checker('', "Even"), True)
    
    def test_full_cases(self):
        self.assertEqual(packet_checker('10010010', "Even"), True)
        self.assertEqual(packet_checker('10010011', "Even"), False)
        self.assertEqual(packet_checker('10010010', "Odd"), False)
        self.assertEqual(packet_checker('10010011', "Odd"), True)
        self.assertEqual(packet_checker('00011000', "Even"), False)
        self.assertEqual(packet_checker('100010101011010101010011', "Even"), False)
        self.assertEqual(packet_checker('000011010110111101101001', "Odd"), False)

if __name__ == "__main__":
    unittest.main()