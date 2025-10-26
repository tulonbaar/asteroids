import pygame
import constants
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        angle = random.uniform(0, 360)
        speed = random.uniform(50, 150)
        self.velocity = pygame.Vector2(1, 0).rotate(angle) * speed

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

        # Wrap around screen edges
        if self.position.x < -self.radius:
            self.position.x = constants.SCREEN_WIDTH + self.radius
        elif self.position.x > constants.SCREEN_WIDTH + self.radius:
            self.position.x = -self.radius
        if self.position.y < -self.radius:
            self.position.y = constants.SCREEN_HEIGHT + self.radius
        elif self.position.y > constants.SCREEN_HEIGHT + self.radius:
            self.position.y = -self.radius