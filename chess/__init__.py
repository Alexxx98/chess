from .board import Board
from .piece import Pon, Bishop, Knight, Rook, Queen, King


chess_board = Board()

# Set starting position for all pieces
# Pons
for line in chess_board.board:
    for index, field in enumerate(line):
        if index == 1:
            field.place_piece(Pon("assets/pieces/Chess_pdt60.png", "black"))

        if index == 6:
            field.place_piece(Pon("assets/pieces/Chess_plt60.png", "white"))

# Rooks
for field in (chess_board.board[0][0], chess_board.board[7][0]):
    field.place_piece(Rook("assets/pieces/Chess_rdt60.png", "black"))

for field in (chess_board.board[0][7], chess_board.board[7][7]):
    field.place_piece(Rook("assets/pieces/Chess_rlt60.png", "white"))

# Knights
for field in (chess_board.board[1][0], chess_board.board[6][0]):
    field.place_piece(Knight("assets/pieces/Chess_ndt60.png", "black"))

for field in (chess_board.board[1][7], chess_board.board[6][7]):
    field.place_piece(Knight("assets/pieces/Chess_nlt60.png", "white"))

# Bishops
for field in (chess_board.board[2][0], chess_board.board[5][0]):
    field.place_piece(Bishop("assets/pieces/Chess_bdt60.png", "black"))

for field in (chess_board.board[2][7], chess_board.board[5][7]):
    field.place_piece(Bishop("assets/pieces/Chess_blt60.png", "white"))

# Queens
chess_board.board[3][0].place_piece(Queen("assets/pieces/Chess_qdt60.png", "black"))
chess_board.board[3][7].place_piece(Queen("assets/pieces/Chess_qlt60.png", "white"))

# Kings
chess_board.board[4][0].place_piece(King("assets/pieces/Chess_kdt60.png", "black"))
chess_board.board[4][7].place_piece(King("assets/pieces/Chess_klt60.png", "white"))
