import unittest
from golden_master import GoldenMaster
from trivia import Game
from trivia_refactored import GameRefactored

class TestSameGoldenMaster(unittest.TestCase):
    def setUp(self) -> None:
        game_instance = Game()
        self.golden_master = GoldenMaster(game_instance)
        game_instance_2 = GameRefactored()
        self.golden_master_2 = GoldenMaster(game_instance_2)
    
    def test_same_game(self):
        self.golden_master.run_and_capture_output()
        self.golden_master_2.run_and_capture_output()
        result = self.golden_master.compare_to_golden_master(self.golden_master_2.captured_outputs)
        self.assertEqual(result, True)
