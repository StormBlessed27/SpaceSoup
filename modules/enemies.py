import pygame, random
from modules import options

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = pygame.image.load(img).convert()
        self.image.set_colorkey(options.BLACK)
        self.rect = self.image.get_rect(  )
        self.rect.x =random.randrange(options.WIDTH-self.rect.width)
        self.rect.y =random.randrange(-100, -40)
        self.speedy = 3
        self.speedx = random.randrange(-5,5)


    def Move(self):
      self.rect.y +=self.speedy
      self.rect.x += self.speedx
      if self.rect.top > options.HEIGHT+10 or self.rect.left< -20 or self.rect.right>options.WIDTH+20:
          self.rect.x =random.randrange(options.WIDTH-self.rect.width)
          self.rect.y =random.randrange(-100, -40)
          self.speedy = 3
    
    def IncreaseSpeed(self):
        pass
