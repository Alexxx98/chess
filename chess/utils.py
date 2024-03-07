import pygame


def set_custom_cursor(cursor, surface: pygame.Surface) -> None:
    pygame.mouse.set_visible(False)
    cursor_rect = cursor.get_rect()
    cursor_rect.center = pygame.mouse.get_pos()
    surface.blit(cursor, cursor_rect)
    pygame.display.update()
