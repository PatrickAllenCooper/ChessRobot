####################
# Patrick Cooper   #
# Chess Playing AI #
# 10-25-19          #
####################

################################
# sets the state for a new game
################################


import chess.engine
from boardvis import visboard
from stockfish import Stockfish

#board = visboard.board


def get_board_state():
    board = visboard.board


# please use appropriate file path
stockfish = Stockfish('C:/Users/patri/PycharmProjects/chess-ai/stockfish_10_x64.exe')

# set position by sequence of moves:
stockfish.set_position(['e2e4', 'e7e6'])

# set position by Forsyth–Edwards Notation (FEN):
stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2")

print(stockfish.get_best_move()) # d2d4
print(stockfish.is_move_correct('a2a3')) # True

# get last move info:
print(stockfish.info)
# e.g. 'info depth 2 seldepth 3 multipv 1 score mate -1 nodes 11 nps 5500 tbhits 0 time 2 pv h2g1 h4g3'

# set current engine's skill level:
stockfish.set_skill_level(15)

# get current engine's parameters:
stockfish.get_parameters()