import pygame

pygame.init()

# Create the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Square")

# Set up our colours
SKY_BLUE = (135, 206, 235)
PICKLED_PINK = (245, 127, 187)
BURP = (255, 233, 110)

# Store the player's and enemy starting position
player_x = 375
player_y = 275
enemy_x = 100
enemy_y = 200

# Control how many pixels the square moves each frame
speed = 0.5
enemy_speed = 0.1

# Keep the game running
running = True

while running:

    # Check for events, including closing the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keyboard keys are being pressed
    keys = pygame.key.get_pressed()

    # Check which keyboard keys are being pressed
    keys = pygame.key.get_pressed()

    # Move left by decreasing the X position
    if keys[pygame.K_LEFT]:
        player_x = player_x - speed

    # Move right by increasing the X position
    if keys[pygame.K_RIGHT]:
        player_x = player_x + speed

    # Move up by decreasing the Y position
    if keys[pygame.K_UP]:
        player_y = player_y - speed

    # Move down by increasing the Y position
    if keys[pygame.K_DOWN]:
        player_y = player_y + speed

    # Move left by decreasing the X position

    if enemy_x < player_x:
        enemy_x += enemy_speed
    elif enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    elif enemy_y > player_y:
        enemy_y -= enemy_speed

    # 1. Create rectangle objects for both the player and the enemy
    player_rect = pygame.Rect(player_x, player_y, 50, 50)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 30, 30)

    # 2. Check if the rectangles overlap (collision)
    if player_rect.colliderect(enemy_rect):
        running = False #Ends the game loop

    # Paint the background to clear the previous frame
    screen.fill(SKY_BLUE)

    # Draw the square at its current position
    pygame.draw.rect(screen, PICKLED_PINK, (player_x, player_y, 50, 50))
    pygame.draw.rect(screen, BURP, (enemy_x, enemy_y, 30, 30))

    # Show the updated screen
    pygame.display.flip()

pygame.quit()