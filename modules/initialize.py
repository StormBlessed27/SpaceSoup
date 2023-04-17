import pygame

from modules import SpaceShip, options, enemies, Bullet


def initialize():
  
  #Initialize screen and pygame motor

  
  pygame.init()
  pygame.mixer.init()
  EVENT_INCREASE_SPEED = pygame.USEREVENT+1
  pygame.time.set_timer(EVENT_INCREASE_SPEED, 30000,7)
  screen = pygame.display.set_mode((options.WIDTH, options.HEIGHT))
  background = pygame.image.load(options.BACKGROUND_IMG)
  pygame.display.set_caption("Space Soup")
  gameClock = pygame.time.Clock()
  is_running = True

  #Load Sound Effects
  bullet_sound=pygame.mixer.Sound(options.Laser_SD)
  explosion_sound=pygame.mixer.Sound(options.Explosion_SD)


  sprites = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  ship = SpaceShip.spaceShip()
  sprites.add(ship)
  bullet=Bullet.Bullet(0,0)
  bullets=pygame.sprite.Group()



  for i in range(9):
    if i%2 ==0:
      asteroid = enemies.Asteroid(options.MED_ASTEROID_IMG)
    else:
      asteroid = enemies.Asteroid(options.BIG_ASTEROID_IMG)
    sprites.add(asteroid)
    asteroids.add(asteroid)



  while is_running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        is_running = False
      if event.type == EVENT_INCREASE_SPEED:
        for asteroid in asteroids:
          asteroid.IncreaseSpeed()

      elif event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
          ship.shoot(sprites,bullets)
          bullet_sound.play()
          
    for bullet in bullets:
      bullet.Move()

    screen.blit(background,(0,0))
    ship.Move()
    ship.Limit()
    for asteroid in asteroids:
      asteroid.Move()
      print(asteroid.speedy)



    #Colide - ship vs meteor
    hits =pygame.sprite.spritecollide(ship,asteroids, True)
    if hits:
      is_running=False

    #Colide - bullet vs meteor 
    hits=pygame.sprite.groupcollide(asteroids,bullets,True,True)
    for hit in hits:
      asteroid=enemies.Asteroid(options.ASTEROID_IMG)
      sprites.add(asteroid)
      asteroids.add(asteroid)
      explosion_sound.play()
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

    
    gameClock.tick(60)
