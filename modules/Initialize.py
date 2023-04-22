import pygame, random

from modules import Asteroid, Bullet, Options, SpaceShip


def initialize():
  
  #Initialize screen and pygame motor
  pygame.init()
  pygame.mixer.init()
  EVENT_INCREASE_SPEED = pygame.USEREVENT+1
  EVENT_AUTO_SHOOT = pygame.USEREVENT+2
  pygame.time.set_timer(EVENT_INCREASE_SPEED, 30000,7)
  pygame.time.set_timer(EVENT_AUTO_SHOOT,500 )
  screen = pygame.display.set_mode((Options.WIDTH, Options.HEIGHT))
  background = pygame.image.load(Options.BACKGROUND_IMG)
  pygame.display.set_caption("Space Soup")
  gameClock = pygame.time.Clock()
  is_running = True

  #Load Sound Effects
  bullet_sound=pygame.mixer.Sound(Options.BULLET_SD)
  explosion_sound=pygame.mixer.Sound(Options.EXPLOSION_SD)


  sprites = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  ship = SpaceShip.spaceShip()
  sprites.add(ship)
  bullet=Bullet.Bullet(0,0)
  bullets=pygame.sprite.Group()



  for i in range(9):
    if i%2 ==0:
      asteroid = Asteroid.Asteroid(Options.MED_ASTEROID_IMG_1)
    else:
      asteroid = Asteroid.Asteroid(Options.BIG_ASTEROID_IMG_1)
    sprites.add(asteroid)
    asteroids.add(asteroid)



  while is_running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        is_running = False
      if event.type == EVENT_INCREASE_SPEED:
        Asteroid.Asteroid.IncreaseSpeed()

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
    
    #hits =pygame.sprite.spritecollide(ship,asteroids, True)
    #if hits:
    #  is_running=False

    #Colide - bullet vs meteor 
    hits=pygame.sprite.groupcollide(asteroids,bullets,True,True)
    for hit in hits:
      asteroid = None
      if random.randint(0,1) == 1:
        asteroid=Asteroid.Asteroid(Options.BIG_ASTEROID_IMG_1)
      else:
        asteroid = asteroid=Asteroid.Asteroid(Options.MED_ASTEROID_IMG_1)
      sprites.add(asteroid)
      asteroids.add(asteroid)
      explosion_sound.play()
    sprites.update()
    sprites.draw(screen)

    pygame.display.flip()

    
    gameClock.tick(60)
