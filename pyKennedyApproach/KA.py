import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
MEDIUM_LIGHT_BLUE = (135, 206, 250)
FUCHSIA = (255, 119, 255)
RED = (255, 0, 0)

# Set the dimensions of the grid and the size of each dot
GRID_DIMENSIONS = (20, 20)
DOT_SIZE = (4, 2)

# Set the screen size and initialize Pygame
SCREEN_SIZE = (800, 600)
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# Define a font for the text
font = pygame.font.SysFont('monospace', 20, bold=True)

# Define a function to convert coordinates to screen coordinates
def get_screen_coords(x, y):
    x_offset = int((screen.get_width() - (GRID_DIMENSIONS[0] * DOT_SIZE[0])) / 2)
    y_offset = int(font.get_height() * 4)
    return (x_offset + (x * DOT_SIZE[0]), y_offset + (y * DOT_SIZE[1]))

# Set the title of the window
pygame.display.set_caption("Kennedy Approach")

# Set the background color
screen.fill(FUCHSIA)

# Draw the text area
text_rect = pygame.Rect(0, 0, SCREEN_SIZE[0], font.get_height() * 4)
pygame.draw.rect(screen, MEDIUM_LIGHT_BLUE, text_rect)

# Draw the text
text = font.render("KENNEDY APPROACH", True, BLACK)
text_rect = text.get_rect(center=(SCREEN_SIZE[0] / 2, font.get_height() * 2))
screen.blit(text, text_rect)

# Draw the runway
runway_start = get_screen_coords(11, 15)
runway_end = get_screen_coords(13, 15)
pygame.draw.line(screen, BLACK, runway_start, runway_end, 3)
runway_text = font.render("JFK", True, BLACK)
runway_text_rect = runway_text.get_rect(center=(runway_start[0] + ((runway_end[0] - runway_start[0]) / 2), runway_start[1] + font.get_height()))
screen.blit(runway_text, runway_text_rect)

# Draw the grid dots
grid_rect = pygame.Rect(0, text_rect.bottom, SCREEN_SIZE[0], SCREEN_SIZE[1] - text_rect.height)
pygame.draw.rect(screen, MEDIUM_LIGHT_BLUE, grid_rect)
for y in range(GRID_DIMENSIONS[1]):
    for x in range(GRID_DIMENSIONS[0]):
        dot_rect = pygame.Rect(get_screen_coords(x, y), DOT_SIZE)
        pygame.draw.rect(screen, BLACK, dot_rect)

# Update the display
pygame.display.flip()

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit the game
pygame.quit()
