import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Initialize the delta time variable
    dt = 0

    # Create groups for game objects
    updatable = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shootables = pygame.sprite.Group()

    # Set each game object's containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shootables, updatable, drawable)

    # Create a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Create an asteroid field object
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black color
        screen.fill((0, 0, 0))
        
        # Update all game objects
        for obj in updatable:
            obj.update(dt)
        
        # Check for collisions
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                sys.exit("Game over!")
            for shot in shootables:
                if asteroid.check_collision(shot):
                    asteroid.kill()
                    shot.kill()

        # Draw all game objects
        for obj in drawable:
            obj.draw(screen)

        # Update the display with the new frame
        pygame.display.flip()
        
        # Cap frame rate at 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

# Initialize the game
if __name__ == "__main__":
    main()
