"""
Similar to Caesar Encrypt, just reverse the process. Simple, right?

Challenge notes:
Do not shift non-alphabetic characters (numbers, symbols etc.)

Challenge ID: 1b3f455bac04a946
"""

def caesar_decrypt(ciphertext: str, s: int) -> str:
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
        self.assertEqual(caesar_decrypt("Khoor", 3), "Hello")
        self.assertEqual(caesar_decrypt("Ebiil", -3), "Hello")
        self.assertEqual(caesar_decrypt("Khoor123", 3), "Hello123")
    
    def test_full_cases(self):
        self.assertEqual(caesar_decrypt("Mjqqt, Btwqi!", 3), "Hello, World!")
        self.assertEqual(caesar_decrypt("Xxvpwo Zfedmo", -3), "Caesar Cipher")
        self.assertEqual(caesar_decrypt("Hnb Kdc Wx", 17), "Yes But No")
        self.assertEqual(caesar_decrypt("1r_7g1r_z_ek4f?", -25), "1s_7h1s_a_fl4g?")
        self.assertEqual(caesar_decrypt("dszf1o_t_x4v3_d0xp_cpq3cpyn3d?", 15), "shou1d_i_m4k3_s0me_ref3renc3s?")
        self.assertEqual(caesar_decrypt("u4_r4mpy0!", 21), "z4_w4rud0!")
        self.assertEqual(caesar_decrypt("Ptwj lf, Wjvznjr if", 255), "Kore ga, Requiem da")
        self.assertEqual(caesar_decrypt("n4y_f_4cctg3_l7_es3_7cfes_0q_es1d_n1as3cepi7?", 22051999587), "c4n_u_4rriv3_a7_th3_7ruth_0f_th1s_c1ph3rtex7?") # if someone actually does 22 billion shifts on the alphabet Im gonna be impressed
    
    def test_invalid_cases(self):
        # Not applicable for this challenge
        return 0
    
if __name__ == "__main__":
    unittest.main()