import pygame, sys

from modules import options, spaceShip


def initialize():
  pygame.init()
  screen = pygame.display.set_mode((options.WINDOW_WIDTH, options.WINDOW_HEIGHT))
  gameClock = pygame.time.Clock()
  ship = spaceShip.spaceShip(options.WINDOW_WIDTH/2, options.WINDOW_HEIGHT/2, options.SHIPSPEED)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    screen.fill('Black')

    

    ship.Move()
    ship.Draw(screen)

    if ship.rect.top <=0 or ship.rect.bottom >= options.WINDOW_HEIGHT:
      if ship.rect.top <= 0: ship.rect.top=0
      if ship.rect.bottom >= options.WINDOW_HEIGHT: ship.rect.bottom = options.WINDOW_HEIGHT
    if ship.rect.left <=0 or ship.rect.right >= options.WINDOW_WIDTH:
      if ship.rect.left <= 0: ship.rect.left=0
      if ship.rect.right >= options.WINDOW_WIDTH: ship.rect.right=options.WINDOW_WIDTH

    

    pygame.display.update()
    gameClock.tick(60)


