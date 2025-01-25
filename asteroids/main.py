from asteroidfield import AsteroidField
from constants import *
import pygame

from player import Player
from asteroid import Asteroid
from shot import Shot


def main() -> None:
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    dt: float = 0

    # Groups (sao tipo interfaces)
    updatables: pygame.sprite.Group = pygame.sprite.Group()
    drawables: pygame.sprite.Group = pygame.sprite.Group()
    asteroids: pygame.sprite.Group = pygame.sprite.Group()
    bullets: pygame.sprite.Group = pygame.sprite.Group()

    AsteroidField.containers = (updatables,)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    Shot.containers = (
        updatables,
        drawables,
        bullets,
    )

    player: Player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField: AsteroidField = AsteroidField()

    RUN: bool = True
    while RUN:
        # Update screen
        screen.fill("#000000")

        # Update
        for updatable in updatables:
            updatable.update(dt)

        # Draw
        for drawable in drawables:
            drawable.draw(screen)

        # show display
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        for asteroid in asteroids:
            if player.checkCollision(asteroid):
                print("Game Over!")
                RUN = False
            for bullet in bullets:
                if bullet.checkCollision(asteroid):
                    asteroid.split()
                    bullet.kill()

        dt = clock.tick(FPS) / 1000


if __name__ == "__main__":
    main()
