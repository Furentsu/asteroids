import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create a clock object to control the frame rate
    clock = pygame.time.Clock()

    # Initialize the delta time variable
    dt = 0

    # Create a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black color
        screen.fill((0, 0, 0))
        
        # Update the player
        player.update(dt)

        # Draw the player
        player.draw(screen)

        # Update the display with the new frame
        pygame.display.flip()
        
        # Cap frame rate at 60 FPS and calculate delta time
        dt = clock.tick(60) / 1000

# Initialize the game
if __name__ == "__main__":
    main()
