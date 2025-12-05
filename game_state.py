"""
game_state represents the game board, players location on the board and the current player to play a move.
"""
class game_state:

    def __init__(self, grid, location_1, location_2, curr_player):
        """
        :param grid: matrix that represents the grid during this turn
        :param location_1: player 1 location in this turn
        :param location_2: player 2 location in this turn
        :param curr_player: the player that its turn currently
        """
        self.__grid = grid
        self.__player_locations = {1: location_1, 2: location_2}
        self.__grid[location_1] = 1
        self.__grid[location_2] = 2
        self.__curr_player = curr_player

    def get_grid(self):
        return self.__grid

    def get_player_locations(self):
        return self.__player_locations

    def get_curr_player(self):
        return self.__curr_player

    def set_curr_player(self, curr_player):
        self.__curr_player = curr_player

    def get_prev_player_location(self):    # used to get the current other player location
        return self.__player_locations[(self.__curr_player % 2) + 1]

    def get_curr_player_location(self):
        return self.__player_locations[self.__curr_player]

    def add_moves_in_direction(self, curr_location, direction, moves):   # adds legal moves in a certain direction(tuple) into moves list
        """
        :param curr_location: location of current player
        :param direction: add legal moves from this direction
        :param moves: list to add the new moves
        """
        curr_location = (curr_location[0] + direction[0], curr_location[1] + direction[1])
        if self.is_legal_location(curr_location):
            moves.append(curr_location)

    def potential_moves(self):
        """
        :return: list of all legal moves for the current player
        """
        moves = []
        curr_location = self.__player_locations[self.__curr_player]

        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i) == abs(j) or i == 0 or j == 0:     # skip invalid knight moves
                    continue
                self.add_moves_in_direction(curr_location, (i, j), moves)
        return moves

    def get_moves(self):         # generates all possible game states after a legal move, switching the current player for each new state, all neighboring states
        """
        :return: All possible game_state objects after performing a legal move during this turn
        for each new game_state, we switch the current player to the other player.
        """
        moves = self.potential_moves()
        new_games = []

        for move in moves:
            if self.__curr_player == 1:
                new_games.append(game_state(self.__grid.copy(), move, self.__player_locations[2], 2))
            else:
                new_games.append(game_state(self.__grid.copy(), self.__player_locations[1], move, 1))

        return new_games

    def is_legal_location(self, curr_location):
        """
        :param curr_location: the location we want to check
        :return: True if curr_location is a legal location for current player to move to, False otherwise
        """
        if (curr_location[0] < 0 or curr_location[0] >= len(self.__grid)
                or curr_location[1] < 0 or curr_location[1] >= len(self.__grid[1])):    # checking boundaries
            return False
        return self.__grid[curr_location] == 0                                 # checking if the cell is not visited

    def is_terminal(self):
        """
        :return:  True if there are no legal moves for the current player and False otherwise.
        """
        p_location = self.__player_locations[self.__curr_player]

        for i in range(-2, 3):
            for j in range(-2, 3):
                if abs(i) == abs(j) or i == 0 or j == 0:   # skip invalid knight moves checks
                    continue
                curr_location = (p_location[0] + i, p_location[1] + j)
                if self.is_legal_location(curr_location):
                    return False    # found a legal move
        return True  # no legal moves found

    def apply_move(self, move):
        """
        :param move: to be applied on the current player
        move the current player and switch the turn to the opposing player.
        """
        self.__grid[move] = self.__curr_player
        self.__player_locations[self.__curr_player] = move
        self.__curr_player = (self.__curr_player % 2) + 1

    def get_score(self):
        """
        :return: the current score of the game.
        value = 1000 points is just an arbitrary high number, you can change its value.
        This value is large enough so that the heuristic value will be between 1000 and -1000.
        """
        value = 1000
        if self.__curr_player == 1:
            #No moves for the first player (first player lost)
            return value * -1
        #First player won
        return value
