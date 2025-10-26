import pygame
import constants
from player import Player
from asteroidfield import AsteroidField
from asteroids import Asteroid
from shot import Shot

def create_game_objects():
    """Create and return all game objects and groups"""
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
    
    return updatables, drawables, asteroids, shots, player1, asteroid_field

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
    
    # Initialize font for text rendering
    font_large = pygame.font.Font(None, 74)
    font_medium = pygame.font.Font(None, 36)
    
    # Game states
    PLAYING = "playing"
    GAME_OVER = "game_over"
    game_state = PLAYING
    
    # Create initial game objects
    updatables, drawables, asteroids, shots, player1, asteroid_field = create_game_objects()

    while True:
        dt = clock.tick(60) / 1000  # Amount of seconds since last frame

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_state == GAME_OVER:
                    # Restart the game
                    game_state = PLAYING
                    # Clear all sprite groups
                    updatables.empty()
                    drawables.empty()
                    asteroids.empty()
                    shots.empty()
                    # Create new game objects
                    updatables, drawables, asteroids, shots, player1, asteroid_field = create_game_objects()
            
        screen.fill((0, 0, 0))
        
        if game_state == PLAYING:
            updatables.update(dt)
            
            # Check for collisions between player and asteroids
            for asteroid in asteroids:
                if player1.collides_with(asteroid):
                    game_state = GAME_OVER
                    break
            
            for drawable in drawables:
                drawable.draw(screen)
        
        elif game_state == GAME_OVER:
            # Draw all game objects (frozen)
            for drawable in drawables:
                drawable.draw(screen)
            
            # Draw Game Over text
            game_over_text = font_large.render("Game Over!", True, (255, 255, 255))
            restart_text = font_medium.render("Press spacebar to restart", True, (255, 255, 255))
            
            # Center the text on screen
            game_over_rect = game_over_text.get_rect(center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2 - 50))
            restart_rect = restart_text.get_rect(center=(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2 + 20))
            
            screen.blit(game_over_text, game_over_rect)
            screen.blit(restart_text, restart_rect)
            
        pygame.display.flip()

if __name__ == "__main__":
    main()
