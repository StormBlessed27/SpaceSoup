import pygame, random
from modules import Opciones

class Asteroid(pygame.sprite.Sprite):

    speedy = Opciones.SPEED

    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(Opciones.BLACK)
        self.rect = self.image.get_rect(  )
        self.rect.x =random.randrange(Opciones.WIDTH-self.rect.width)
        self.rect.y =random.randrange(-100, -40)
        self.speedx = random.randrange(-5,5)


    def Move(self):
      """Se encarga de mover el asteroide"""
      self.rect.y +=self.speedy
      self.rect.x += self.speedx
      if self.rect.top > Opciones.HEIGHT+10 or self.rect.left< -20 or self.rect.right>Opciones.WIDTH+20:
          self.rect.x =random.randrange(Opciones.WIDTH-self.rect.width)
          self.rect.y =random.randrange(-100, -40)
    
    def IncreaseSpeed():
        """Aumenta la velocidad de caida de los asteroides"""
        Asteroid.speedy += 1
