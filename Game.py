import pygame


def check_collision(player, walls):
    """
    -------------------------------------------------------
    Checks whether the player collides with any of the maze walls.
    -------------------------------------------------------
    Parameters:
       player - the rectangle representing the player (pygame.Rect)
       walls - a list of rectangles representing the maze walls (list)
    Returns:
       collision - True if the player collides with a wall,
                   False otherwise (bool)
    -------------------------------------------------------
    """
    for wall in walls:
        if player.colliderect(wall):
            return True
    return False


pygame.init()

# Set screen resolution
SCREEN_WIDTH = 850
SCREEN_HEIGHT = 900

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Maze Game")

# Set up colours
WHITE = (255, 255, 255)
BLUE = (192, 210, 255)
RED = (255, 192, 192)
GREEN = (192, 235, 192)
BLACK = (0, 0, 0)

# Set up the player
player_x = 30
player_y = 30
player_size = 25
speed = 3

# Create the exit
exit_rect = pygame.Rect(800, 850, 30, 30)

# Create the maze walls
walls = [
    pygame.Rect(75, 50, 20, 150),
    pygame.Rect(75, 50, 160, 20),
    pygame.Rect(150, 50, 20, 75),
    pygame.Rect(150, 125, 175, 20),
    pygame.Rect(305, 50, 20, 75),
    pygame.Rect(320, 125, 175, 20),
    pygame.Rect(475, 50, 20, 90),
    pygame.Rect(390, 0, 20, 75),
    pygame.Rect(490, 50, 225, 20),
    pygame.Rect(390, 145, 20, 75),
    pygame.Rect(390, 215, 105, 20),
    pygame.Rect(475, 225, 20, 90),
    pygame.Rect(575, 125, 20, 110),
    pygame.Rect(575, 125, 140, 20),
    pygame.Rect(305, 315, 450, 20),
    pygame.Rect(305, 217, 20, 230),
    pygame.Rect(150, 217, 175, 20),
    pygame.Rect(150, 225, 20, 110),
    pygame.Rect(75, 315, 95, 20),
    pygame.Rect(0, 427, 225, 20),
    pygame.Rect(225, 315, 20, 132),
    pygame.Rect(75, 540, 345, 20),
    pygame.Rect(400, 425, 20, 132),
    pygame.Rect(420, 425, 250, 20),
    pygame.Rect(650, 215, 200, 20),
    pygame.Rect(750, 315, 20, 245),
    pygame.Rect(475, 540, 275, 20),
    pygame.Rect(650, 540, 20, 135),
    pygame.Rect(400, 540, 20, 135),
    pygame.Rect(650, 655, 200, 20),
    pygame.Rect(400, 655, 180, 20),
    pygame.Rect(75, 540, 20, 275),
    pygame.Rect(235, 540, 20, 275),
    pygame.Rect(155, 650, 20, 300),
    pygame.Rect(235, 815, 150, 20),
    pygame.Rect(320, 650, 20, 95),
    pygame.Rect(325, 725, 150, 20),
    pygame.Rect(455, 725, 20, 200),
    pygame.Rect(560, 660, 20, 240),
    pygame.Rect(650, 725, 20, 240),
    pygame.Rect(650, 725, 125, 20),
    pygame.Rect(755, 725, 20, 100),

]

# Set up the game
clock = pygame.time.Clock()
running = True
won = False

# Main game loop
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    if not won:

        # Move left
        if keys[pygame.K_LEFT]:
            player_x -= speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_x += speed

        # Move right
        if keys[pygame.K_RIGHT]:
            player_x += speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_x -= speed

        # Move up
        if keys[pygame.K_UP]:
            player_y -= speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_y += speed

        # Move down
        if keys[pygame.K_DOWN]:
            player_y += speed
            player = pygame.Rect(player_x, player_y, player_size, player_size)

            if check_collision(player,walls) == True:
                player_y -= speed

        # Keep the player inside the screen
        if player_x < 0:
            player_x = 0

        if player_x > SCREEN_WIDTH - player_size:
            player_x = SCREEN_WIDTH - player_size

        if player_y < 0:
            player_y = 0

        if player_y > SCREEN_HEIGHT - player_size:
            player_y = SCREEN_HEIGHT - player_size

        # Update the player rectangle
        player = pygame.Rect(player_x, player_y, player_size, player_size)

        # Check if the player reaches the exit
        if player.colliderect(exit_rect):
            won = True

    # Draw the background
    screen.fill(WHITE)

    # Draw the maze walls
    for wall in walls:
        pygame.draw.rect(screen, BLUE, wall)

    # Draw the exit
    pygame.draw.rect(screen, GREEN, exit_rect)

    # Draw the player
    player = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, RED, player)

    # Display the winning message
    if won:
        font = pygame.font.SysFont(None, 75)
        message = font.render("LEVEL 1: COMPLETED!", True, BLACK)
        screen.blit(message, (125, 425))

    # Update the display
    pygame.display.flip()

    # Limit the game to 60 FPS
    clock.tick(60)

# Close Pygame
pygame.quit()