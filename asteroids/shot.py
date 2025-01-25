from typing import override
from circleshape import CircleShape
from constants import *
import pygame


class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 1)
        self.velocity.scale_to_length(PLAYER_SHOT_SPEED)

    @override
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt

    def rotate(self, angle):
        self.velocity = self.velocity.rotate(angle)
