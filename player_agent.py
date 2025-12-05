from game_state import game_state

class player_agent:

    def __init__(self, strategy):
        self.strategy = strategy    # using Strategy Design Pattern

    def get_next_move(self, _game_state):
        #copy the current game state
        curr_state = game_state(_game_state.get_grid().copy(), _game_state.get_player_locations()[1], _game_state.get_player_locations()[2], _game_state.get_curr_player())
        value, best_state = self.run_strategy(curr_state)   # returns the best next game_state after making a move and the value of that state
        #return the prev player location because game_state switches players turn after it makes a move
        return best_state.get_prev_player_location()   # the move is represented by the location the player moved to

    def run_strategy(self, curr_state):    # using Strategy Design Pattern
        return self.strategy(curr_state)

class player_agent_heuristics(player_agent):
    def __init__(self, strategy, heuristic, depth=1):   # depth is the max depth to search
        super().__init__(strategy)
        self.heuristic = heuristic
        self.depth = depth

    def run_strategy(self, curr_state):
        return self.strategy(curr_state, self.heuristic, self.depth)
