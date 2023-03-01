# import the Pygame library
import pygame

# initialize Pygame and set up the game window
pygame.init()
screen = pygame.display.set_mode((800, 600))

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# create a game object to represent the player's character
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((50, 50))
    self.image.fill(WHITE)
    self.rect = self.image.get_rect()
    self.rect.center = (400, 300)

  def update(self):
    # move the player based on keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.rect.x -= 5
    if keys[pygame.K_RIGHT]:
      self.rect.x += 5
    if keys[pygame.K_UP]:
      self.rect.y -= 5
    if keys[pygame.K_DOWN]:
      self.rect.y += 5

# create a sprite group to hold the player
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# game loop
running = True
while running:
  # process events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # update the game state
  all_sprites.update()

  # draw the game
  screen.fill(BLACK)
  all_sprites.draw(screen)
  pygame.display.flip()

# clean up and exit
pygame.quit()