import pygame, sys
from modules import options, spaceShip, Asteroid

def initialize():

  pygame.init()
  screen = pygame.display.set_mode((options.WIDTH, options.HEIGHT))
  pygame.display.set_caption("Space Soup")
  gameClock = pygame.time.Clock()
  
  #Game Background
  background=pygame.image.load(options.Background_IMAGE)

  #Sprites-group
  all_sprites=pygame.sprite.Group()
  Asteroid_list=pygame.sprite.Group()
  Bullets=pygame.sprite.Group()


  #Player
  ship=spaceShip.spaceShip()
  all_sprites.add(ship)

  #Asteroid
  asteroid=Asteroid.Asteroid()
  Asteroid_list.add(asteroid)
  all_sprites.add(asteroid)

  #limites
  def limits():
    if ship.rect.top <=0 or ship.rect.bottom >= options.HEIGHT:
      if ship.rect.top <= 0: ship.rect.top=0
      if ship.rect.bottom >= options.HEIGHT: ship.rect.bottom = options.HEIGHT
    if ship.rect.left <=0 or ship.rect.right >= options.WIDTH:
      if ship.rect.left <= 0: ship.rect.left=0
      if ship.rect.right >= options.WIDTH: ship.rect.right=options.WIDTH


  is_running=True
  while is_running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        is_running=False
      
      
    screen.blit(background,(0,0))
    ship.Move()
    asteroid.Move()
    all_sprites.update()
    all_sprites.draw(screen)
    limits()

    hits=pygame.sprite.spritecollide(ship,Asteroid_list,True)
    if hits:
      is_running=False

    pygame.display.flip()
    gameClock.tick(60)
