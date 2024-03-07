import pygame
from chess.settings import (
    WIDTH,
    HEIGHT,
    FPS,
    BACKGROUND_IMAGE,
    GRAB_CURSOR,
    GC_WIDTH,
    GC_HEIGHT,
)
from chess import chess_board
from chess.utils import set_custom_cursor


pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load(BACKGROUND_IMAGE)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

grab_cursor = pygame.image.load(GRAB_CURSOR)
grab_cursor = pygame.transform.scale(grab_cursor, (GC_WIDTH, GC_HEIGHT))

clock = pygame.time.Clock()


def main():
    running: bool = True
    holding: bool = False
    held_piece = None
    legal_fields = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for left click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for line in chess_board.board:
                    for field in line:
                        if mouse_pos[0] in range(
                            field.x, field.x + field.width
                        ) and mouse_pos[1] in range(field.y, field.y + field.height):
                            if field.piece:
                                holding = True
                                held_piece = field.piece
                                previous_field = field
                                legal_fields = held_piece.valid_moves(field.get_pos(), chess_board.board)

            if event.type == pygame.MOUSEMOTION:
                mouse_pos = pygame.mouse.get_pos()
                if holding:
                    held_piece.x = mouse_pos[0] - field.width // 2
                    held_piece.y = mouse_pos[1] - field.height // 2
                    held_piece.draw_piece(WINDOW)

            if event.type == pygame.MOUSEBUTTONUP:
                holding = False
                valid_field = False
                pygame.mouse.set_visible(True)
                pos1, pos2 = held_piece.get_piece_center()
                for line in chess_board.board:
                    for field in line:
                        if (
                            pos1 in range(field.x, field.x + field.width)
                            and pos2 in range(field.y, field.y + field.height)
                            and field.check_piece_color(held_piece)
                            and field in legal_fields
                        ):
                            valid_field = True
                            held_piece.x = field.x
                            held_piece.y = field.y
                            previous_field.piece = None
                            field.piece = held_piece

                if not valid_field:
                    held_piece.x = previous_field.x
                    held_piece.y = previous_field.y

        if holding:
            set_custom_cursor(grab_cursor, WINDOW)

        WINDOW.blit(background, (0, 0))
        chess_board.draw_the_board(WINDOW)

        for row in chess_board.board:
            for field in row:
                if field.piece:
                    field.piece.draw_piece(WINDOW)

        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
