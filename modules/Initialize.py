import pygame, random

from modules import Asteroid, Bullet, SpaceShip, Options, Score, GameOver


def initialize():
  
  #Inicializando el motor pygame y el motor de sonido de pygame.
  pygame.init()
  pygame.mixer.init()

  #creando nuevos eventos
  EVENT_INCREASE_SPEED = pygame.USEREVENT+1
  EVENT_AUTO_SHOOT = pygame.USEREVENT+2
  EVENT_SCORE_TIME = pygame.USEREVENT+3

  #Creando temporizadores para los eventos
  pygame.time.set_timer(EVENT_INCREASE_SPEED, 1000,7)
  pygame.time.set_timer(EVENT_AUTO_SHOOT,300 )
  pygame.time.set_timer(EVENT_SCORE_TIME, 2000)

  #inicializando la ventana, el fondo de pantalla, el titulo de la pantalla y el reloj de juego 
  screen = pygame.display.set_mode((Options.WIDTH, Options.HEIGHT))
  background = pygame.image.load(Options.BACKGROUND_IMG)
  pygame.display.set_caption("Space Soup")
  gameClock = pygame.time.Clock()

  #variable controladore del ciclo de juego
  is_running = True

  #Cargando efectos de sonido
  bullet_sound=pygame.mixer.Sound(Options.BULLET_SD)
  explosion_sound=pygame.mixer.Sound(Options.EXPLOSION_SD)

  #Conjunto de sprites
  sprites = pygame.sprite.Group()
  #Conjunto de asteroides
  asteroids = pygame.sprite.Group()
  #Astronave del jugador
  ship = SpaceShip.spaceShip()
  #Se añade la nave al conjunto de sprites
  sprites.add(ship)
  #Creando la bala
  bullet=Bullet.Bullet(0,0)
  #creando el conjunto de balas
  bullets=pygame.sprite.Group()

  #Inicializamos el marcador
  score = 0

  #Pantalla de Game Over
  game_over = True

  #Creacion de los asteroides
  for i in range(9):
    if i%2 ==0:
      asteroid = Asteroid.Asteroid(Options.MED_ASTEROID_IMG_1)
    else:
      asteroid = Asteroid.Asteroid(Options.BIG_ASTEROID_IMG_1)
    sprites.add(asteroid)
    asteroids.add(asteroid)

  #Iniciando el ciclo de juego
  while is_running:

    if game_over:
      
      show_go_screen()
      game_over = False
      sprites = pygame.sprite.Group()
      asteroids = pygame.sprite.Group()
      bullets=pygame.sprite.Group()

      for i in range(9):
        if i%2 ==0:
          asteroid = Asteroid.Asteroid(Options.MED_ASTEROID_IMG_1)
        else:
          asteroid = Asteroid.Asteroid(Options.BIG_ASTEROID_IMG_1)
        sprites.add(asteroid)
        asteroids.add(asteroid)

        score = 0

    #Ciclo de eventos
    for event in pygame.event.get():

      #Evento quit
      if event.type == pygame.QUIT:
        pygame.quit()
        is_running = False
      #Evento de aumento de velocidad
      if event.type == EVENT_INCREASE_SPEED:
        Asteroid.Asteroid.IncreaseSpeed()

      
      if event.type==EVENT_AUTO_SHOOT:
        ship.shoot(sprites,bullets)
        bullet_sound.play()
      
      #Evento de aumento de puntos por tiempo
      if event.type == EVENT_SCORE_TIME:
        score +=1
        
    for bullet in bullets:
      bullet.Move()


    #Añadiendo el fondo de pantalla
    screen.blit(background,(0,0))

    #Movimiento de la nave
    ship.Move()
    #Limites con la pantalla
    ship.Limit()

    #Moviendo los asteroides
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
      score += 10
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
    game_over = True
    
    Score.Score.draw_text(screen, str(score),  25, Options.WIDTH//2, 10)
    pygame.display.flip()

    
    gameClock.tick(60)
