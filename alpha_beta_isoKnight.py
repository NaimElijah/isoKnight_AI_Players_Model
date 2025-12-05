import math

# entry point for MAX player, that uses a_b_minimax with alpha-beta pruning function refactored here
def alphabeta_max(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None

    alpha = -math.inf
    beta = math.inf
    v = -math.inf
    best_move = None

    moves = current_game.get_moves()
    for move in moves:
        mx, _ = a_b_minimax(move, alpha, beta)
        if mx > v:
            v = mx
            best_move = move
        # update alpha for MAX
        alpha = max(alpha, v)    # the max player only cares about maximizing alpha
        # (optional) we could break here if v >= beta, but not strictly needed at root

    return v, best_move


# entry point for MIN player, that uses a_b_maximin with alpha-beta pruning function refactored here
def alphabeta_min(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None

    alpha = -math.inf
    beta = math.inf
    v = math.inf
    best_move = None

    moves = current_game.get_moves()
    for move in moves:
        mx, _ = a_b_maximin(move, alpha, beta)
        if mx < v:
            v = mx
            best_move = move
        # update beta for MIN
        beta = min(beta, v)     # the min player only cares about minimizing beta
        # (optional) we could break here if v <= alpha, but not strictly needed at root

    return v, best_move









def a_b_maximin(current_game, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    best_move = None
    moves = current_game.get_moves()

    for move in moves:
        mx, _ = a_b_minimax(move, alpha, beta)
        if mx > v:
            v = mx
            best_move = move
        # added code here for alpha-beta algorithm  <--
        # alpha-beta pruning condition for MAX node
        if v >= beta:
            # pruning: as instructed in the assignment, return (v, None)
            return v, None

        alpha = max(alpha, v)
        # added code here for alpha-beta algorithm <--
    return v, best_move




def a_b_minimax(current_game, alpha=-math.inf, beta=math.inf):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    best_move = None
    moves = current_game.get_moves()

    for move in moves:
        mx, _ = a_b_maximin(move, alpha, beta)
        if mx < v:
            v = mx
            best_move = move

        # added code here for alpha-beta algorithm <--
        # alpha-beta pruning condition for MIN node
        if v <= alpha:
            # pruning: as instructed in the assignment, return (v, None)
            return v, None
        beta = min(beta, v)
        # added code here for alpha-beta algorithm <--
    return v, best_move
