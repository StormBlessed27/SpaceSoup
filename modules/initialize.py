import pygame

from modules import SpaceShip, options, enemies, Bullet


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
  bullet=Bullet.Bullet(0,0)
  bullets=pygame.sprite.Group()


  for i in range(9):
    asteroid = enemies.Asteroid(options.ASTEROID_IMG)
    sprites.add(asteroid)
    asteroids.add(asteroid)

  while is_running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        is_running = False

      elif event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
          ship.shoot(sprites,bullets)
                 
    for bullet in bullets:
      bullet.Move()

    screen.blit(background,(0,0))
    ship.Move()
    ship.Limit()
    for asteroid in asteroids:
      asteroid.Move()

    #Colide - ship vs meteor
    hits =pygame.sprite.spritecollide(ship,asteroids, True)
    if hits:
      is_running=False

    #Colide - bullet vs meteor 
    hits=pygame.sprite.groupcollide(asteroids,bullets,True,True)
    for hit in hits:
      pass


   
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()
    
    gameClock.tick(60)
