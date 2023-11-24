class GameRefactored:
    def __init__(self):
        self.players = []
        self.places = [0] * 6
        self.purses = [0] * 6
        self.in_penalty_box = [0] * 6
        self.questions = {
            'Pop': ["Pop Question %s" % i for i in range(50)],
            'Science': ["Science Question %s" % i for i in range(50)],
            'Sports': ["Sports Question %s" % i for i in range(50)],
            'Rock': [self.create_rock_question(i) for i in range(50)]
        }
        self.current_player = 0
        self.is_getting_out_of_penalty_box = False

    def create_rock_question(self, index):
        return "Rock Question %s" % index

    def is_playable(self):
        return self.how_many_players >= 2

    def add(self, player_name):
        self.players.append(player_name)
        self.places[self.how_many_players] = 0
        self.purses[self.how_many_players] = 0
        self.in_penalty_box[self.how_many_players] = False
        print(f"{player_name} was added")
        print(f"They are player number {len(self.players)}")
        return True

    @property
    def how_many_players(self):
        return len(self.players)
    
    def roll(self, roll):
        print(f"{self.players[self.current_player]} is the current player")
        print(f"They have rolled a {roll}")
        self._handle_penalty_box(roll)
        self._move_player_and_ask_question(roll)

    def _handle_penalty_box(self, roll):
        if self.in_penalty_box[self.current_player]:
            self.is_getting_out_of_penalty_box = roll % 2 != 0
            outcome = 'getting out of' if self.is_getting_out_of_penalty_box else 'not getting out of'
            print(f"{self.players[self.current_player]} is {outcome} the penalty box")

    def _move_player_and_ask_question(self, roll):
        if not self.in_penalty_box[self.current_player] or self.is_getting_out_of_penalty_box:
            self.places[self.current_player] = (self.places[self.current_player] + roll) % 12
            print(f"{self.players[self.current_player]}'s new location is {self.places[self.current_player]}")
            print(f"The category is {self._current_category}")
            self._ask_question()

    def _ask_question(self):
        print(self.questions[self._current_category].pop(0))

    @property
    def _current_category(self):
        categories = ['Pop', 'Science', 'Sports', 'Rock']
        return categories[self.places[self.current_player] % len(categories)]

    def was_correctly_answered(self):
        winner = True
        if self.in_penalty_box[self.current_player] and self.is_getting_out_of_penalty_box:
            winner = self._handle_correct_answer_and_check_win("Answer was correct!!!!")
        elif not self.in_penalty_box[self.current_player]:
            winner = self._handle_correct_answer_and_check_win("Answer was corrent!!!!")
        self._update_current_player()
        return winner
    
    def _handle_correct_answer_and_check_win(self, message: str) -> bool:
        self._handle_correct_answer(message)
        return self._did_player_win()
    
    def _handle_correct_answer(self, message: str) -> None:
        print(message)
        self.purses[self.current_player] += 1
        print(f"{self.players[self.current_player]} now has {self.purses[self.current_player]} Gold Coins.")
   
    def _update_current_player(self) -> None:
        self.current_player = (self.current_player + 1) % len(self.players)
    
    def wrong_answer(self):
        print('Question was incorrectly answered')
        print(f"{self.players[self.current_player]} was sent to the penalty box")
        self.in_penalty_box[self.current_player] = True
        self._update_current_player()
        return True

    def _did_player_win(self):
        return self.purses[self.current_player] != 6