import pygame, random

from modules import Options

class Asteroid(pygame.sprite.Sprite):
    """Clase Asteroide"""
    speedy = Options.SPEED
    def __init__(self, img):
        """Crea un asteroide y le establece una velocidad en x y en y"""
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(Options.BLACK)
        self.rect = self.image.get_rect(  )
        self.rect.x =random.randrange(Options.WIDTH-self.rect.width)
        self.rect.y =random.randrange(-100, -40)
        self.speedx = random.randrange(-5,5)

    def Move(self):
      """Se encarga de mover el asteroide"""
      self.rect.y +=self.speedy
      self.rect.x += self.speedx
      if self.rect.top > Options.HEIGHT+10 or self.rect.left< -20 or self.rect.right>Options.WIDTH+20:
          self.rect.x =random.randrange(Options.WIDTH-self.rect.width)
          self.rect.y =random.randrange(-100, -40)
    
    def IncreaseSpeed():
        """Aumenta la velocidad de caida de los asteroides"""
        Asteroid.speedy += 1
    def RestoreInitSpeed():
        """Devuelve la velocidad original a los asteroides"""
        Asteroid.speedy = Options.SPEED
