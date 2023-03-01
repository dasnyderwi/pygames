import pygame

# define the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define the hexagonal grid parameters
WIDTH = 50
HEIGHT = 50

# initialize the pygame library
pygame.init()

# create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# define the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# define the hexagon vertices
vertices = [(0, -HEIGHT / 2), (WIDTH / 2, -HEIGHT / 4),
            (WIDTH / 2, HEIGHT / 4), (0, HEIGHT / 2),
            (-WIDTH / 2, HEIGHT / 4), (-WIDTH / 2, -HEIGHT / 4)]

# define the function to draw a hexagon
def draw_hexagon(x, y, color, surface):
  translated_vertices = []
  for vx, vy in vertices:
    translated_vertices.append((vx + x, vy + y))
  pygame.draw.polygon(surface, color, translated_vertices)

# define the function to generate the hexagonal grid
def generate_grid(width, height, surface):
  for i in range(width):
    for j in range(height):
      draw_hexagon(i * WIDTH, j * HEIGHT * 3 / 4, BLACK, surface)

# generate the hexagonal grid
generate_grid(10, 10, screen)

# keep the window open until the user closes it
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

# quit the pygame library
pygame.quit()