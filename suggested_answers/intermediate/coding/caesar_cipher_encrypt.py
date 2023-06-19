"""
Given a string plaintext and a shift key s, write a program
that will encrypt the plaintext using the Caesar Cipher and return the 
result

The Caesar Cipher is a basic method of encrypting messages, which involves shifting each
letter in the plaintext by a set number of places (determined by the shift key) up or down the
alphabet. A negative shift value would indicate a left shift down the alphabet, while a positive
shift value would indicate a right shift

Examples:
caesar_encrypt("Hello", 3) -> "Khoor"
caesar_encrypt("Fubar", 3) -> "Ixedu"
caesar_encrypt("Hello", -3) -> "Ebiil"
caesar_encrypt("Hello123", 3) -> "Khoor123"

Challenge notes:
Do not shift non-alphabetic characters (numbers, symbols etc.)

Challenge ID: 16814d93170c8911
"""

def caesar_encrypt(plaintext: str, s: int) -> str:
    # Your code here
    return ""

######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

import unittest
class Test_TemplateChallenge(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(caesar_encrypt("Hello", 3), "Khoor")
        self.assertEqual(caesar_encrypt("Hello", -3), "Ebiil")
        self.assertEqual(caesar_encrypt("Hello123", 3), "Khoor123")
    
    def test_full_cases(self):
        self.assertEqual(caesar_encrypt("Hello, World!", 3), "Mjqqt, Btwqi!")
        self.assertEqual(caesar_encrypt("Caesar Cipher", -3), "Xxvpwo Zfedmo")
        self.assertEqual(caesar_encrypt("Yes But No", 17), "Hnb Kdc Wx")
        self.assertEqual(caesar_encrypt("1s_7h1s_a_fl4g?", -25), "1r_7g1r_z_ek4f?")
        self.assertEqual(caesar_encrypt("PEIRCE", 15), "APTCNP")
        self.assertEqual(caesar_encrypt("cOmpu7ing", 21), "hTruz7nsl")
        self.assertEqual(caesar_encrypt("Kore ga, Requiem da", 255), "Ptwj lf, Wjvznjr if")
        self.assertEqual(caesar_encrypt("lets_use_a_really_loooongggggg_string", 11), "wped_fdp_l_cplwwj_wzzzzyrrrrrr_dectyr")
    
    def test_invalid_cases(self):
        # Not applicable for this challenge
        return 0
    
if __name__ == "__main__":
    unittest.main()