from io import StringIO
import sys
from random import seed, randrange

class GoldenMaster:
    def __init__(self, game):
        self.game = game
        self.captured_outputs = []

    def run_and_capture_output(self):
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        self.game_play()
        self.captured_outputs.append(sys.stdout.getvalue())
        sys.stdout = original_stdout

    def game_play(self):
        not_a_winner = False
        seed(42)
        self.game.add('Roberto')
        self.game.add('Luis')
        self.game.add('Diego')

        while True:
            self.game.roll(randrange(5) + 1)

            if randrange(9) == 7:
                not_a_winner = self.game.wrong_answer()
            else:
                not_a_winner = self.game.was_correctly_answered()

            if not not_a_winner:
                break

    def compare_to_golden_master(self, other_recorded_outputs) -> bool:
        if self.captured_outputs == other_recorded_outputs:
            return True
        else:
            return False
