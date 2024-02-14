import pygame
from settings import WIDTH, HEIGHT, FPS, BLACK, WHITE


pygame.init()

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        WINDOW.fill(BLACK)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
