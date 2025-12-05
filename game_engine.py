import numpy as np
import minimax_isoKnight
import alpha_beta_isoKnight, heuristic_alpha_beta_isoKnight, heuristics
from game_state import game_state
from player_agent import player_agent, player_agent_heuristics

def print_current_state(curr_state, player_turn):
    print(f"Current player is player {player_turn},"
          f" moved to {curr_state.get_player_locations()[player_turn]}."
          f"\nThe board is:\n"
          f"{curr_state.get_grid()}")

def play_isoKnight(player_1, player_2, init_state):                              #     <<--------------- RUNS THE BASE GAME
    players = {1: player_1, 2: player_2}
    curr_player = player_1
    player_turn = 1
    curr_state = init_state
    print(f"start board is:\n{curr_state.get_grid()}")
    while not curr_state.is_terminal():
        chosen_move = curr_player.get_next_move(curr_state)   # get the move(indices to move to) from the current player
        curr_state.apply_move(chosen_move)                    # apply the move to the current game state
        print_current_state(curr_state, player_turn)          # print the current state of the game
        player_turn = curr_state.get_curr_player()            # switch player turn
        curr_player = players[player_turn]                    # switch current player
    print(f"\n\nPlayer {(player_turn % 2) + 1} is the winner!!")

def play_with_minimax():                                                         # RUNS THE GAME WITH MINIMAX MODE, with already given maximin/minimax strategies
    player_1 = player_agent(minimax_isoKnight.maximin)
    player_2 = player_agent(minimax_isoKnight.minimax)
    grid = np.zeros((3, 3), dtype=int)
    init_state = game_state(grid, (0, 1), (2, 1), 1)
    play_isoKnight(player_1, player_2, init_state)





def play_with_alpha_beta():                                                      # RUNS THE GAME WITH ALPHA_BETA MODE
    player_1 = player_agent(alpha_beta_isoKnight.alphabeta_max)
    player_2 = player_agent(alpha_beta_isoKnight.alphabeta_min)
    grid = np.zeros((4, 4), dtype=int)
    init_state = game_state(grid, (0, 0), (3, 3), 1)
    play_isoKnight(player_1, player_2, init_state)


def play_with_heuristics():                                                       # RUNS THE GAME WITH BASE HEURISTICS MODE
    depth_player_1 = 6
    depth_player_2 = 6

    # try different depths, you can change the depth numbers, board size and locations, for example:
    # depth_player_1 = 6, depth_player_2 = 1      or     depth_player_1 = 1, depth_player_2 = 6

    player_1 = player_agent_heuristics(heuristic_alpha_beta_isoKnight.alphabeta_max_h, heuristics.base_heuristic, depth_player_1)
    player_2 = player_agent_heuristics(heuristic_alpha_beta_isoKnight.alphabeta_min_h, heuristics.base_heuristic, depth_player_2)
    grid = np.zeros((6, 6), dtype=int)
    init_state = game_state(grid, (0, 0), (3, 3), 1)
    play_isoKnight(player_1, player_2, init_state)


def play_with_advanced_heuristics():                                              # RUNS THE GAME WITH ADVANCED HEURISTICS MODE
    depth_player_1 = 3
    depth_player_2 = 3
    #Does player 1 wins most of the games you play?
    player_1 = player_agent_heuristics(heuristic_alpha_beta_isoKnight.alphabeta_max_h, heuristics.advanced_heuristic, depth_player_1)
    player_2 = player_agent_heuristics(heuristic_alpha_beta_isoKnight.alphabeta_min_h, heuristics.base_heuristic, depth_player_2)
    grid = np.zeros((10, 10), dtype=int)
    init_state = game_state(grid, (0, 0), (3, 3), 1)
    play_isoKnight(player_1, player_2, init_state)


if __name__ == '__main__':
    # play_with_minimax()
    # play_with_alpha_beta()
    play_with_heuristics()
    # play_with_advanced_heuristics()