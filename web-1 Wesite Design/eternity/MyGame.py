import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RPG Game")

# Load background image
background_image = pygame.image.load("galaxy.jpg")
background_image = pygame.transform.scale(background_image, (width, height))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 255, 0)
RED = (255, 0, 0)

# Button attributes
button_width = 200
button_height = 50
button_padding = 20

# Game states
GAME_MENU = 0
GAME_PLAYING = 1
GAME_OPTIONS = 2
game_state = GAME_MENU

# RPG game variables
player_health = 100
player_damage = 10
enemy_health = 50
enemy_damage = 5

# Game loop
running = True
while running:
    screen.blit(background_image, (0, 0))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == GAME_MENU:
                if start_button_rect.collidepoint(event.pos):
                    game_state = GAME_PLAYING
                    print("Start the game!")
            elif options_button_rect.collidepoint(event.pos):
                    game_state = GAME_OPTIONS
                    print("Open options menu!")
            elif exit_button_rect.collidepoint(event.pos):
                    print("Exiting the game!")
                    pygame.quit()
                    sys.exit()
            elif game_state == GAME_OPTIONS:
                if back_button_rect.collidepoint(event.pos):
                    game_state = GAME_MENU
                    print("Back to the main menu!")

    if game_state == GAME_MENU:
        # Draw buttons for the main menu
        start_button_rect = pygame.draw.rect(screen, BLACK, (
            (width - button_width) // 2,
            (height - (button_height * 3 + button_padding * 2)) // 2,
            button_width, button_height))
        pygame.draw.rect(screen, RED, (
            (width - button_width) // 2,
            (height - (button_height * 3 + button_padding * 2)) // 2 + button_height + button_padding,
            button_width, button_height))
        pygame.draw.rect(screen, RED, (
            (width - button_width) // 2,
            (height - (button_height * 3 + button_padding * 2)) // 2 + 2 * (button_height + button_padding),
            button_width, button_height))

        # Button labels for the main menu
        font = pygame.font.SysFont(None, 30)
        start_text = font.render("Start", True, WHITE)
        screen.blit(start_text, (
            (width - start_text.get_width()) // 2,
            (height - (button_height * 3 + button_padding * 2)) // 2 + button_height // 2 - start_text.get_height() // 2))
        options_text = font.render("Options", True, WHITE)
        screen.blit(options_text, (
            (width - options_text.get_width()) // 2,
            (height - (button_height * 3 + button_padding * 2)) // 2 + button_height + button_padding + button_height // 2 - options_text.get_height() // 2))
        exit_text = font.render("Exit", True, WHITE)
        screen.blit(exit_text, (
            (width - exit_text.get_width()) // 2,
            (height - (button_height * 3 + button_padding * 2)) // 2 + 2 * (button_height + button_padding) + button_height // 2 - exit_text.get_height() // 2))

    elif game_state == GAME_PLAYING:
        # RPG game logic
        player_health -= enemy_damage
        enemy_health -= player_damage

        # Draw game elements
        font = pygame.font.SysFont(None, 40)
        player_health_text = font.render("Player Health: " + str(player_health), True, WHITE)
        enemy_health_text = font.render("Enemy Health: " + str(enemy_health), True, WHITE)
        screen.blit(player_health_text, (20, 20))
        screen.blit(enemy_health_text, (20, 60))

        # Check game over condition
        if player_health <= 0 or enemy_health <= 0:
            game_state = GAME_MENU

    elif game_state == GAME_OPTIONS:
        # Draw buttons for the options menu
        back_button_rect = pygame.draw.rect(screen, BLACK, (
            (width - button_width) // 2,
            (height - button_height) // 2,
            button_width, button_height))

        # Button labels for the options menu
        font = pygame.font.SysFont(None, 30)
        back_text = font.render("Back", True, WHITE)
        screen.blit(back_text, (
            (width - back_text.get_width()) // 2,
            (height - button_height) // 2 + button_height // 2 - back_text.get_height() // 2))

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
sys.exit()
