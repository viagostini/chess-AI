from os import system

import time
import random

import chess

from evaluate_board import evaluate
from minimaxAB import minimaxAB_player
from utils import who, display_board, clear_output

def play_game(player1, player2, visual="simple", pause=0.1):
    """
    Takes two player functions and play a game between them
    
    param: visual
        can be either 'simple' or None

    param: pause
        delay between moves
    """
    board = chess.Board()

    while not board.is_game_over(claim_draw=True):
        start_time = time.time()
        if board.turn == chess.WHITE:
            uci = player1(board)
        else:
            uci = player2(board)
        elapsed_time = time.time() - start_time

        name = who(board.turn)
        board.push_uci(uci)
        board_stop = display_board(board)
        game_str = "Move %s %s, Play '%s' in %s seconds\n%s" % (
                        len(board.move_stack), name, uci, str(elapsed_time), board_stop)
        
        if visual is not None:
            clear_output()
            print(game_str)
            time.sleep(pause)
   
    result = None
    if board.is_checkmate():
        msg = "checkmate: " + who(not board.turn) + " wins!"
        result = not board.turn
    elif board.is_stalemate():
        msg = "draw: stalemate"
    elif board.is_fivefold_repetition():
        msg = "draw: 5-fold repetition"
    elif board.is_insufficient_material():
        msg = "draw: insufficient material"
    elif board.can_claim_draw():
        msg = "draw: claim"
    if visual is not None:
        print(msg)
    
    return (result, msg, board)




if __name__ == "__main__":
    play_game(minimaxAB_player, minimaxAB_player, visual='simple', pause=0.1)