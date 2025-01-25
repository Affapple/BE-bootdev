import random
from typing import override
from circleshape import CircleShape
import pygame

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius: float = self.radius - ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child2 = Asteroid(self.position.x, self.position.y, new_radius)

        rand_angle: float = random.uniform(20, 50)
        child1.velocity = self.velocity.rotate(rand_angle) * 1.2
        child2.velocity = self.velocity.rotate(-rand_angle) * 1.2
