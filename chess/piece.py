import pygame
from .settings import FIELD_WIDTH, FIELD_HEIGHT

from typing import Tuple


class Piece:
    def __init__(self, image, color):
        self._image = image
        self.color = color
        self.x = None
        self.y = None
        self.width = FIELD_WIDTH
        self.height = FIELD_HEIGHT

    @property
    def image(self) -> str:
        return self._image

    def draw_piece(self, surface: pygame.Surface) -> None:
        piece = pygame.image.load(self._image)
        piece = pygame.transform.scale(piece, (self.width, self.height))
        surface.blit(piece, (self.x, self.y))

    def get_piece_center(self) -> Tuple[int, int]:
        return (self.x + self.width // 2, self.y + self.height // 2)

    def valid_color(self, piece) -> bool:
        if self.color == piece.color:
            return False
        return True
    
    def is_on_board(self, board, pos1, pos2):
        try:
            return board[pos1][pos2]
        except IndexError:
            pass
    

class Pon(Piece):
    pass

class Bishop(Piece):
    pass

class Knight(Piece):
    def valid_moves(self, starting_pos: Tuple[int, int], board):
        pos1, pos2 = starting_pos
        possible_moves = [
            (pos1 - 1, pos2 - 2),
            (pos1 + 1, pos2 - 2),
            (pos1 - 2, pos2 - 1),
            (pos1 + 2, pos2 - 1),
            (pos1 - 2, pos2 + 1),
            (pos1 + 2, pos2 + 1),
            (pos1 - 1, pos2 + 2),
            (pos1 + 1, pos2 + 2),
        ]

        legal_moves = list(map(lambda pos: self.is_on_board(board, pos[0], pos[1]), possible_moves))
        return legal_moves


class Rook(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass