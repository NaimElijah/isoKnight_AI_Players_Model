import numpy as np

def base_heuristic(curr_state):
    curr_player_save = curr_state.get_curr_player()

    curr_state.set_curr_player(1)  # switch to player 1
    p1_moves = len(curr_state.potential_moves())
    curr_state.set_curr_player(2)  # switch to player 2
    p2_moves = len(curr_state.potential_moves())

    curr_state.set_curr_player(curr_player_save)  # restore the original current player
    return p1_moves - p2_moves


# Advanced heuristic function: (thought of factors that can affect the game)
def advanced_heuristic(curr_state):
    """
    A stronger heuristic that combines:
    - Direct mobility (legal moves count)
    - Secondary mobility (future moves from each move)
    - Positional factors (distance, board edges)
    """
    original_player = curr_state.get_curr_player()

    # Factor Number 1: Direct mobility for both players
    curr_state.set_curr_player(1)
    p1_moves = curr_state.potential_moves()
    curr_state.set_curr_player(2)
    p2_moves = curr_state.potential_moves()
    mobility_score = len(p1_moves) - len(p2_moves)                     # 1st Factor calculated


    # Factor Number 2: Secondary mobility (how many moves each move leads to)
    # This helps detect whether a move leads into a dead end.
    def secondary_mobility(moves, player):
        curr_state.set_curr_player(player)
        total = 0
        for move in moves:
            r, c = move
            future = 0
            for i in range(-2, 3):
                for j in range(-2, 3):
                    if abs(i) == abs(j) or i == 0 or j == 0:
                        continue
                    nr, nc = r + i, c + j
                    if 0 <= nr < len(curr_state.get_grid()) and 0 <= nc < len(curr_state.get_grid()[0]) and curr_state.get_grid()[nr, nc] == 0:
                        future += 1
            total += future
        return total

    sec_p1 = secondary_mobility(p1_moves, 1)
    sec_p2 = secondary_mobility(p2_moves, 2)

    secondary_score = (sec_p1 - sec_p2) * 0.5                          # 2nd Factor calculated


    # Factor Number 3: Positional factor: distance between players
    # Being closer reduces mobility; too far is also bad.
    locs = curr_state.get_player_locations()
    p1_loc = np.array(locs[1])
    p2_loc = np.array(locs[2])
    distance = np.linalg.norm(p1_loc - p2_loc)

    # We *reward* keeping a reasonable distance (not too close)
    # Encourages P1 to maintain an optimal spacing (not too close)
    distance_score = (distance - 2) * 0.3                               # 3rd Factor calculated


    # Factor Number 4: Edge penalties - knights near borders are weaker
    def edge_penalty(loc):
        r, c = loc
        h = len(curr_state.get_grid())
        w = len(curr_state.get_grid()[0])
        return int(r == 0 or r == h - 1 or c == 0 or c == w - 1)
    # Good if P2 is more restricted by edges than P1
    edge_score = (edge_penalty(p2_loc) - edge_penalty(p1_loc)) * 0.4     # 4th Factor calculated


    curr_state.set_curr_player(original_player)
    # Combining all the Factor's influences together to make the final advanced heuristic value     # Total Advanced Heuristic calculated
    return mobility_score + secondary_score + distance_score + edge_score

