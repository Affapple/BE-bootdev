from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    RUN = True
    while RUN:
        screen.fill("#000000")
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False


if __name__ == "__main__":
    main()
