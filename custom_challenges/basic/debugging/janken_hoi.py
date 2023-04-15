"""
Simple enoough program to play Janken (Scissors - Paper - Stone) with the
player right? Well, apparently not for this programmer...

Task: 
Fix the following function such that it functions as according
to the win and lose conditions. 

Win/Lose conditions:
Standard scissors, paper, stone win conditions

Fail conditions:
User inputs something other than "Scissors", "Paper", "Stone" (not case sensitive), 
return "Invalid choice selected"

Challenge ID: 
"""

def janken_hoi(P1_move: str, P2_move: str) -> str:
    if P1_move == "" and P2_move == "":
        return "Invalid choice selected"
    elif isinstance(P1_move, (int, bool)) or isinstance(P2_move, (int, bool)):
        return "Invalid choice selected"
    else:
        P1_standard, P2_standard = P1_move.lower(), P2_move.lower()
        if P1_standard == P2_standard:
            return "Tie"
        elif (P1_standard == "scissors" and P2_standard = "paper") or (P1_standard = "paper" and P2_standard == "stone") or (P1_standard == "stone" and P2_standard == "scissors"):
            return "Player 2 wins!"
        elif (P2_standard == "scissors" and P1_standard == "paper") or (P2_standard == "paper" and P1_standard == "stone") or (P2_standard == "stone" and P1_standard == "scissors"):
            return "Player 1 wins!"
        else:
            return "Invalid choice selected"
    
######################################################
#                                                    #
#                   Test Cases                       #
#                  Do Not Modify                     #
#                                                    #
######################################################

import unittest
class Test_JankenHoi(unittest.TestCase):
    def test_edge_cases(self):
        self.assertEqual(janken_hoi("Scissors", "Paper"), "Player 1 wins!")
        self.assertEqual(janken_hoi("Paper", "Scissors"), "Player 2 wins!")
        self.assertEqual(janken_hoi("Scissors", "Scissors"), "Tie")
    def test_player_1_win(self):
        self.assertEqual(janken_hoi("Paper", "Stone"), "Player 1 wins!")
        self.assertEqual(janken_hoi("paper", "stone"), "Player 1 wins!")
        self.assertEqual(janken_hoi("PAPER", "STONE"), "Player 1 wins!")
        self.assertEqual(janken_hoi("pAPer", "stONe"), "Player 1 wins!")
    def test_player_2_win(self):
        self.assertEqual(janken_hoi("Stone", "Paper"), "Player 2 wins!")
        self.assertEqual(janken_hoi("stone", "paper"), "Player 2 wins!")
        self.assertEqual(janken_hoi("stone", "PAPER"), "Player 2 wins!")
        self.assertEqual(janken_hoi("stONe", "pAPer"), "Player 2 wins!")
    def test_same_choices(self):
        self.assertEqual(janken_hoi("Paper", "Paper"), "Tie")
        self.assertEqual(janken_hoi("paper", "paper"), "Tie")
        self.assertEqual(janken_hoi("PAPER", "PAPER"), "Tie")
        self.assertEqual(janken_hoi("pAPer", "pAPer"), "Tie")
    def test_invalid_choices(self):
        self.assertEqual(janken_hoi("", "Paper"), "Invalid choice selected")
        self.assertEqual(janken_hoi("Paper", ""), "Invalid choice selected")
        self.assertEqual(janken_hoi("Hmm...", "Paper"), "Invalid choice selected")
        self.assertEqual(janken_hoi(True, False), "Invalid choice selected")
        self.assertEqual(janken_hoi(69, 420), "Invalid choice selected")
        self.assertEqual(janken_hoi("69", "420"), "Invalid choice selected")

if __name__ == "__main__":
    unittest.main()