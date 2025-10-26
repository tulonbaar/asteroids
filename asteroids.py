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

    def split(self):
        # Always kill this asteroid first
        self.kill()
        
        # If this is a small asteroid, just return (don't split)
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        
        # Generate a random angle between 20 and 50 degrees for splitting
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors by rotating the current velocity
        new_velocity_1 = self.velocity.rotate(random_angle)
        new_velocity_2 = self.velocity.rotate(-random_angle)
        
        # Calculate the new radius for the smaller asteroids
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        
        # Create two new asteroids at the current position
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        
        # Set their velocities (scaled up by 1.2 to make them faster)
        asteroid_1.velocity = new_velocity_1 * 1.2
        asteroid_2.velocity = new_velocity_2 * 1.2