from io import StringIO
import sys
import unittest
from golden_master import GoldenMaster
from trivia import Game

class TestGoldenMaster(unittest.TestCase):
    def setUp(self) -> None:
        self.game_instance = Game()
        self.golden_master = GoldenMaster(self.game_instance)
    
    def test_initial_initial_game(self):
        self.assertEqual(self.golden_master.game, self.game_instance)
    
    def test_initial_captured_outputs(self):
        self.assertEqual(self.golden_master.captured_outputs, [])

    def test_run_and_capture_output(self):
        self.golden_master.run_and_capture_output()
        self.assertEqual(len(self.golden_master.captured_outputs), 1)
        self.assertIsInstance(self.golden_master.captured_outputs[0], str)

    def test_game_play(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        self.golden_master.game_play()
        output = sys.stdout.getvalue()
        sys.stdout = original_stdout
        self.assertIsInstance(output, str)

    def test_golden_master_compare_to_golden_master(self):
        self.golden_master.run_and_capture_output()
        result = self.golden_master.compare_to_golden_master(self.golden_master.captured_outputs)
        self.assertEqual(result, True)
    
    def test_golden_master_compare_to_golden_master_failed(self):
        self.golden_master.run_and_capture_output()
        result = self.golden_master.compare_to_golden_master(["test"])
        self.assertEqual(result, False)

