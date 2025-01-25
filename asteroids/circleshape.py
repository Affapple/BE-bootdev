from abc import abstractmethod
import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    @abstractmethod
    def draw(self, screen: pygame.Surface):
        pass

    @abstractmethod
    def update(self, dt: float):
        pass

    def checkCollision(self, other: "CircleShape") -> bool:
        distance: float = self.position.distance_to(other.position)
        return distance <= self.radius + other.radius
