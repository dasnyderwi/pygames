import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 128)
RED = (255, 0, 0)

MEDIUM_DARK_BLUE = (50, 90, 150)
MEDIUM_LT_BLUE = (90, 130, 240)
FUCHSIA = (230, 70, 230)

# Set the dimensions of the grid and the size of each dot
GRID_DIMENSIONS = (20, 20)
DOT_SIZE = (4, 2)

# Set the border between dots and screen edges
HORIZONTAL_BORDER = 20
VERTICAL_BORDER = 30

# Important - Must Init
pygame.init()

# Set the screen size and initialize Pygame
SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# Define a font for the text
font = pygame.font.SysFont('monospace', 20, bold=True)

# Set the title of the window
pygame.display.set_caption("Kennedy Approach")


    
# Draw the background color
screen.fill(MEDIUM_LT_BLUE)

# Draw the text area
#text_rect = pygame.Rect(0, 0, SCREEN_SIZE[0], font.get_height() * 4)
#pygame.draw.rect(screen, FUCHSIA, text_rect)

# Draw the text
#texts = ["Welcome to Kennedy Approach!", "Flight control tower", "Air traffic control"]
#for i, text in enumerate(texts):
    #line = font.render(text, True, BLACK)
    #line_rect = line.get_rect(center=(SCREEN_SIZE[0] / 2, font.get_height() * (i+1) + 10))
    #screen.blit(line, line_rect)
# Draw the text area
text_rect = pygame.Rect(0, 0, SCREEN_SIZE[0], font.get_height() * 5)
pygame.draw.rect(screen, FUCHSIA, text_rect)

# Draw the text
texts = ["Welcome to Kennedy Approach!", "Flight control tower", "Air traffic control", "Enjoy your flight!"]
for i, text in enumerate(texts):
    line = font.render(text, True, BLACK)
    line_rect = line.get_rect(center=(SCREEN_SIZE[0] / 2, font.get_height() * (i+1)))
    screen.blit(line, line_rect)

# Draw the grid
grid_rect = pygame.Rect(HORIZONTAL_BORDER, text_rect.bottom + VERTICAL_BORDER, SCREEN_SIZE[0] - 2 * HORIZONTAL_BORDER, SCREEN_SIZE[1] - text_rect.height - 2 * VERTICAL_BORDER)
pygame.draw.rect(screen, MEDIUM_LT_BLUE, grid_rect)

dot_spacing_x = (grid_rect.width - GRID_DIMENSIONS[0] * DOT_SIZE[0]) // (GRID_DIMENSIONS[0] - 1)
dot_spacing_y = (grid_rect.height - GRID_DIMENSIONS[1] * DOT_SIZE[1]) // (GRID_DIMENSIONS[1] - 1)

for y in range(GRID_DIMENSIONS[1]):
    for x in range(GRID_DIMENSIONS[0]):
        dot_rect = pygame.Rect(grid_rect.left + x * (DOT_SIZE[0] + dot_spacing_x), grid_rect.top + y * (DOT_SIZE[1] + dot_spacing_y), DOT_SIZE[0], DOT_SIZE[1])
        pygame.draw.rect(screen, BLACK, dot_rect)

class Airport:
    def __init__(self, name, grid_pos, size):
        self.name = name
        self.grid_pos = grid_pos
        self.size = size

    def draw(self):
        x, y = self.grid_pos
        w, h = self.size
        rect = pygame.Rect(
            HORIZONTAL_BORDER + x * (DOT_SIZE[0] + dot_spacing_x),
            text_rect.bottom + VERTICAL_BORDER + y * (DOT_SIZE[1] + dot_spacing_y),
            (w-1) * DOT_SIZE[0] + w * dot_spacing_x,
            (h-1) * DOT_SIZE[1] + h * dot_spacing_y,
        )
        pygame.draw.rect(screen, BLACK, rect, 2)

        # Draw the runway
        runway_width = rect.width * 0.8
        runway_height = rect.height * 0.4
        runway_rect = pygame.Rect(rect.centerx - runway_width/2, rect.centery - runway_height/2, runway_width, runway_height)
        pygame.draw.rect(screen, BLACK, runway_rect)

        # Draw the runway stripes
        stripe_width = 1
        stripe_gap = 4
        stripe_length = 5
        num_stripes = int(runway_width / (stripe_width + stripe_gap))

        for i in range(num_stripes):
            stripe_x = runway_rect.left + i * (stripe_width + stripe_gap)
            stripe_rect = pygame.Rect(stripe_x, runway_rect.centery - stripe_width/2, stripe_length, stripe_width)
            pygame.draw.rect(screen, WHITE, stripe_rect)

        # Draw the text label of the airport code in black monospace font
        label = font.render(self.name, True, BLACK)
        label_rect = label.get_rect(center=(rect.centerx, rect.bottom + font.get_height()/2))
        screen.blit(label, label_rect)

# Define the airports
jfk = Airport("JFK", (8, 15), (3, 1))
lax = Airport("LAX", (4, 4), (6, 1))
ord = Airport("ORD", (15, 10), (3, 1))
atl = Airport("ATL", (4, 12), (4, 1))

# Draw the airports
for airport in [jfk, lax, ord, atl]:
    airport.draw()

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

# End of Line
