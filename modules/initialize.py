import pygame

from modules import SpaceShip, options, enemies


def initialize():
  
  #Initialize screen and pygame motor
  pygame.init()
  pygame.mixer.init()
  screen = pygame.display.set_mode((options.WIDTH, options.HEIGHT))
  background = pygame.image.load(options.BACKGROUND_IMG)
  pygame.display.set_caption("Space Soup")
  gameClock = pygame.time.Clock()
  is_running = True
  

  sprites = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  ship = SpaceShip.spaceShip()
  sprites.add(ship)

  for i in range(9):
    asteroid = enemies.Asteroid(options.ASTEROID_IMG)
    sprites.add(asteroid)
    asteroids.add(asteroid)


  while is_running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        is_running = False

    screen.blit(background,(0,0))
    ship.Move()
    ship.Limit()
    for asteroid in asteroids:
      asteroid.Move()
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

    # if ship.rect.top <=0 or ship.rect.bottom >= options.WINDOW_HEIGHT:
    #   if ship.rect.top <= 0: ship.rect.top=0
    #   if ship.rect.bottom >= options.WINDOW_HEIGHT: ship.rect.bottom = options.WINDOW_HEIGHT
    # if ship.rect.left <=0 or ship.rect.right >= options.WINDOW_WIDTH:
    #   if ship.rect.left <= 0: ship.rect.left=0
    #   if ship.rect.right >= options.WINDOW_WIDTH: ship.rect.right=options.WINDOW_WIDT
    
    gameClock.tick(60)



