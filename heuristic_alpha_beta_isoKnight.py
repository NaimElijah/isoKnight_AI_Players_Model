import math
h = None

# Entry point for MAX Player with alpha-beta pruning + heuristic
def alphabeta_max_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    # Terminal or depth cutoff
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None     # so the value we return is the heuristic value of the current game state when depth reached

    alpha = -math.inf
    beta = math.inf
    v = -math.inf
    best_move = None

    moves = current_game.get_moves()
    for move in moves:
        mx, _ = a_b_heu_minimax(move, alpha, beta, depth - 1)
        if mx > v:
            v = mx
            best_move = move
        alpha = max(alpha, v)

    return v, best_move


# Entry point for MIN Player 2 with alpha-beta pruning + heuristic.
def alphabeta_min_h(current_game, _heuristic, depth=3):
    global h
    h = _heuristic
    # Terminal or depth cutoff
    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None     # so the value we return is the heuristic value of the current game state when depth reached

    alpha = -math.inf
    beta = math.inf
    v = math.inf
    best_move = None

    moves = current_game.get_moves()
    for move in moves:
        mx, _ = a_b_heu_maximin(move, alpha, beta, depth - 1)
        if mx < v:
            v = mx
            best_move = move
        beta = min(beta, v)

    return v, best_move








def a_b_heu_maximin(current_game, alpha, beta, depth):
    global h

    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None     # so the value we return is the heuristic value of the current game state when depth reached

    v = -math.inf
    best_move = None

    for move in current_game.get_moves():
        mx, _ = a_b_heu_minimax(move, alpha, beta, depth - 1)

        if mx > v:
            v = mx
            best_move = move

        # MAX pruning
        if v >= beta:
            return v, None
        alpha = max(alpha, v)

    return v, best_move




def a_b_heu_minimax(current_game, alpha, beta, depth):
    global h

    if current_game.is_terminal():
        return current_game.get_score(), None
    if depth == 0:
        return h(current_game), None     # so the value we return is the heuristic value of the current game state when depth reached

    v = math.inf
    best_move = None

    for move in current_game.get_moves():
        mx, _ = a_b_heu_maximin(move, alpha, beta, depth - 1)

        if mx < v:
            v = mx
            best_move = move

        # MIN pruning
        if v <= alpha:
            return v, None
        beta = min(beta, v)

    return v, best_move
