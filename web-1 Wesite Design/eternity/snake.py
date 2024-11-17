import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake initial position and size
snake_x = width // 2
snake_y = height // 2
snake_size = 20

# Snake movement variables
velocity_x = 0
velocity_y = 0
snake_speed = 10

# Fruit position and size
fruit_x = random.randint(0, width - snake_size)
fruit_y = random.randint(0, height - snake_size)
fruit_size = 20

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Game Over flag
game_over = False

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocity_x = -snake_size
                velocity_y = 0
            elif event.key == pygame.K_RIGHT:
                velocity_x = snake_size
                velocity_y = 0
            elif event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -snake_size
            elif event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = snake_size

    # Update snake position
    snake_x += velocity_x
    snake_y += velocity_y

    # Check for collision with fruit
    if abs(snake_x - fruit_x) < snake_size and abs(snake_y - fruit_y) < snake_size:
        score += 1
        fruit_x = random.randint(0, width - snake_size)
        fruit_y = random.randint(0, height - snake_size)

    # Update the display
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (fruit_x, fruit_y, fruit_size, fruit_size))
    pygame.draw.rect(screen, RED, (snake_x, snake_y, snake_size, snake_size))

    # Update score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    # Game Over condition
    if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
        game_over = True

    # Set the game speed
    pygame.time.Clock().tick(snake_speed)

# Quit the game
pygame.quit()
