import pygame
import constants
from player import Player
from asteroidfield import AsteroidField
from asteroids import Asteroid
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    print(f"Asteroid Min Radius: {constants.ASTEROID_MIN_RADIUS}")
    print(f"Asteroid Max Radius: {constants.ASTEROID_MAX_RADIUS}")
    print(f"Asteroid Spawn Rate: {constants.ASTEROID_SPAWN_RATE}")

    print("===============================================================")
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player1 = Player(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2)
    updatables.add(player1)
    drawables.add(player1)

    Asteroid.containers = (updatables, drawables, asteroids)
    Shot.containers = (updatables, drawables, shots)
    AsteroidField.containers = updatables

    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000  # Amount of seconds since last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill((0, 0, 0))
        updatables.update(dt)
        
        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player1.collides_with(asteroid):
                print("Game over!")
                return
        
        for drawable in drawables:
            drawable.draw(screen)
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
