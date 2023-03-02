import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define tile dimensions
TILE_WIDTH = 50
TILE_HEIGHT = 50

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the caption of the window
pygame.display.set_caption("Empire")

# Create a font object
font = pygame.font.Font(None, 36)

# Set the text for the title
title_text = font.render("EMPIRE", True, GREEN)

# Position the title in the center of the screen
title_position = title_text.get_rect(center=(screen_width/2, 50))

# Set the text for the menu options
options_text = font.render("1-Game  2-Load  3-Save  4-Quit", True, WHITE)

# Position the menu options at the bottom of the screen
options_position = options_text.get_rect(center=(screen_width/2, screen_height-50))

# Set the background color
screen.fill(BLACK)

# Draw the title and menu options on the screen
screen.blit(title_text, title_position)
screen.blit(options_text, options_position)

# Draw the sample map
map_width = 8
map_height = 6
for y in range(map_height):
    for x in range(map_width):
        tile_rect = pygame.Rect(x*TILE_WIDTH, y*TILE_HEIGHT+100, TILE_WIDTH, TILE_HEIGHT)
        if (x + y) % 2 == 0:
            pygame.draw.rect(screen, BLUE, tile_rect)
        else:
            pygame.draw.rect(screen, YELLOW, tile_rect)

# Update the display
pygame.display.flip()

# Wait for the user to close the window
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

# Quit Pygame
pygame.quit()
