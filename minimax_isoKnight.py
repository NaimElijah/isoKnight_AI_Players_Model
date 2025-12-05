import math

def maximin(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = -math.inf
    moves = current_game.get_moves()   # gets all possible game states after a legal move
    for move in moves:
        mx, next_move = minimax(move)  # calls minimax on the new game state, on the next player's turn
        if v < mx:
            v = mx
            best_move = move
    return v, best_move

def minimax(current_game):
    if current_game.is_terminal():
        return current_game.get_score(), None
    v = math.inf
    moves = current_game.get_moves()   # gets all possible game states after a legal move
    for move in moves:
        mx, next_move = maximin(move)  # calls maximin on the new game state, on the next player's turn
        if v > mx:
            v = mx
            best_move = move
    return v, best_move

