import pygame

from modules import options, Bullet

class spaceShip(pygame.sprite.Sprite):
    '''Create the player SpaceShip'''
    def __init__(self):
      super().__init__()
      self.image = pygame.image.load(options.SHIP_IMG).convert()
      self.image.set_colorkey(options.BLACK)
      self.rect = self.image.get_rect()
      self.rect.centerx= options.WIDTH//2 
      self.rect.centery= options.HEIGHT//2
      self.speed = options.SPEED

    def Move(self):
      """Move the spaceship"""
      keysState = pygame.key.get_pressed()
      if keysState[pygame.K_d] or keysState[pygame.K_RIGHT]:
        self.rect.x += self.speed 
      elif keysState[pygame.K_a] or keysState[pygame.K_LEFT]:
        self.rect.x -= self.speed

      if keysState[pygame.K_s] or keysState[pygame.K_DOWN]:
        self.rect.y += self.speed
      elif keysState[pygame.K_w] or keysState[pygame.K_UP]:
        self.rect.y -= self.speed

    def Limit(self):
      """Adds colitions with the window limits"""
      if self.rect.top <=0: self.rect.top=0
      if self.rect.bottom >= options.HEIGHT: self.rect.bottom = options.HEIGHT
      if self.rect.left <=0: self.rect.left=0
      if self.rect.right >= options.WIDTH: self.rect.right=options.WIDTH

    
    def shoot(self,sprites,bullets):
      bullet=Bullet.Bullet(self.rect.centerx,self.rect.top)
      sprites.add(bullet)
      bullets.add(bullet)

