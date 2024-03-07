import pygame
from .settings import (
    FIELD_WIDTH,
    FIELD_HEIGHT,
    ROWS,
    COLS,
    X_GAP,
    Y_GAP,
    DARK,
    LIGHT,
)
from .piece import Piece

from typing import Tuple


class Field:
    def __init__(self, row, col, width, height, color):
        self.row = row
        self.col = col
        self.x = row * width + X_GAP
        self.y = col * height + Y_GAP
        self.width = width
        self.height = height
        self.color = color
        self.piece = None

    def __repr__(self) -> str:
        return f"{self.row, self.col}"

    def place_piece(self, piece: Piece) -> None:
        self.piece = piece
        self.piece.x = self.x
        self.piece.y = self.y

    def get_pos(self) -> Tuple[int, int]:
        return (self.row, self.col)

    def check_piece_color(self, piece: Piece) -> bool:
        if not self.piece:
            return True
        return self.piece.valid_color(piece)


class Board:
    def __init__(self) -> None:
        self.board = []
        self.create_the_board()

    def create_the_board(self) -> None:
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    self.board[row].append(
                        Field(row, col, FIELD_WIDTH, FIELD_HEIGHT, LIGHT)
                    )
                else:
                    self.board[row].append(
                        Field(row, col, FIELD_WIDTH, FIELD_HEIGHT, DARK)
                    )

    def draw_the_board(self, surface: pygame.Surface) -> None:
        for row in self.board:
            for field in row:
                pygame.draw.rect(
                    surface,
                    field.color,
                    pygame.Rect(field.x, field.y, field.width, field.height),
                )
