import pygame

from modules import Bullet, Options

class spaceShip(pygame.sprite.Sprite):
    """Crea la astronave del jugador"""
    
    def __init__(self):
      super().__init__()
      self.image = pygame.image.load(Options.SHIP_IMG).convert()
      self.image.set_colorkey(Options.BLACK)
      self.rect = self.image.get_rect()
      self.rect.centerx= Options.WIDTH//2 
      self.rect.centery= Options.HEIGHT//2
      self.speed = Options.SPEED

    def Move(self):
      """Mueve la Astronave"""
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
      """Añade coliciones con los limites de la pantalla"""
      if self.rect.top <=0: self.rect.top=0
      if self.rect.bottom >= Options.HEIGHT: self.rect.bottom = Options.HEIGHT
      if self.rect.left <=0: self.rect.left=0
      if self.rect.right >= Options.WIDTH: self.rect.right=Options.WIDTH

    
    def shoot(self,sprites,bullets):
      """Se encarga de la accion de disparar de la Astronave"""
      bullet=Bullet.Bullet(self.rect.centerx,self.rect.top)
      sprites.add(bullet)
      bullets.add(bullet)

