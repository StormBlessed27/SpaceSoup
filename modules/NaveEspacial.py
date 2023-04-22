import pygame

from modules import Bala, Opciones

class spaceShip(pygame.sprite.Sprite):
    '''Crea la astronave del jugador'''
    
    def __init__(self):
      super().__init__()
      self.image = pygame.image.load(Opciones.SHIP_IMG).convert()
      self.image.set_colorkey(Opciones.BLACK)
      self.rect = self.image.get_rect()
      self.rect.centerx= Opciones.WIDTH//2 
      self.rect.centery= Opciones.HEIGHT//2
      self.speed = Opciones.SPEED

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
      if self.rect.bottom >= Opciones.HEIGHT: self.rect.bottom = Opciones.HEIGHT
      if self.rect.left <=0: self.rect.left=0
      if self.rect.right >= Opciones.WIDTH: self.rect.right=Opciones.WIDTH

    
    def shoot(self,sprites,bullets):
      """Se encarga de la accion de dispara de la Astronave"""
      bullet=Bala.Bullet(self.rect.centerx,self.rect.top)
      sprites.add(bullet)
      bullets.add(bullet)

