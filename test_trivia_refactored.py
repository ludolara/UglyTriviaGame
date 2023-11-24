import unittest
from trivia_refactored import GameRefactored

class TestGameRefactored(unittest.TestCase):
    def setUp(self):
        self.game = GameRefactored()
        self.game.add('Player 1')

    def test_add_player(self):
        self.game.add('Player 2')
        self.assertEqual(len(self.game.players), 2)

    def test_correct_answer_outside_penalty_box(self):
        current_player = self.game.current_player
        self.game.was_correctly_answered()
        self.assertEqual(self.game.purses[current_player], 1)

    def test_correct_answer_inside_penalty_box(self):
        current_player = self.game.current_player
        self.game.wrong_answer()
        self.game.is_getting_out_of_penalty_box = True
        self.game.was_correctly_answered()
        self.assertEqual(self.game.purses[current_player], 1)

    def test_wrong_answer(self):
        current_player = self.game.current_player
        self.game.wrong_answer()
        self.assertEqual(self.game.in_penalty_box[current_player], True)

    def test_roll(self):
        old_place = self.game.places[self.game.current_player]
        self.game.roll(5)
        self.assertEqual(self.game.places[self.game.current_player], (old_place + 5) % 12)

if __name__ == '__main__':
    unittest.main()