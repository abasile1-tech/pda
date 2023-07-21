import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.king_of_hearts = Card("hearts", 10)
        self.queen_of_clubs = Card("clubs", 10)
        self.two_of_diamonds = Card("diamonds", 2)
        self.ace_of_spades = Card("spades", 1)
        self.cards = [self.king_of_hearts, self.queen_of_clubs, self.two_of_diamonds, self.ace_of_spades]

    def test_check_for_ace_function(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.king_of_hearts))
        self.assertEqual(True, CardGame.check_for_ace(self, self.ace_of_spades))

    def test_highest_card_function(self):
        self.assertEqual(self.king_of_hearts, CardGame.highest_card(self, self.king_of_hearts, self.two_of_diamonds))
        self.assertEqual(self.queen_of_clubs, CardGame.highest_card(self, self.queen_of_clubs, self.two_of_diamonds))

    def test_cards_total_function(self):
        self.assertEqual("You have a total of23", CardGame.cards_total(self, self.cards))