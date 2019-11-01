####################
# Patrick Cooper   #
# Chess Playing AI #
# 10-25-19          #
####################


# sets the state for a new game

import chess.engine
from boardvis import visboard

board = visboard.board

def get_board_state():
    board = visboard.board

engine = chess.engine.SimpleEngine.popen_uci("C:/Users/patri/PycharmProjects/chess-ai/stockfish/Windows/stockfish_10_x64.exe")

board = chess.Board()
while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.100))
    board.push(result.move)

engine.quit()