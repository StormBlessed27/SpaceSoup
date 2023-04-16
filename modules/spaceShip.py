import pygame
from modules import options

class spaceShip(pygame.sprite.Sprite):
    '''Create the player SpaceShip'''

    def __init__(self):
       super().__init__()
       self.image = pygame.image.load("assets/images/ship-2.png")
       self.image.set_colorkey("BLACK")
       self.rect=self.image.get_rect()
       self.rect.centerx= options.WINDOW_WIDTH//2
       self.rect.bottom=options.WINDOW_HEIGHT-10
       self.shipSpeed=4
       

    def Move(self):
        teclas_pres = pygame.key.get_pressed()

        if teclas_pres[pygame.K_d] or teclas_pres[pygame.K_RIGHT]:
          self.rect.x += self.shipSpeed 
        elif teclas_pres[pygame.K_a] or teclas_pres[pygame.K_LEFT]:
          self.rect.x -= self.shipSpeed

        if teclas_pres[pygame.K_s] or teclas_pres[pygame.K_DOWN]:
          self.rect.y += self.shipSpeed
        elif teclas_pres[pygame.K_w] or teclas_pres[pygame.K_UP]:
          self.rect.y -= self.shipSpeed

    def Shoot():
        algotambien = 0

 
    def Draw(self, Surface: pygame.Surface):
       shipSurface = pygame.image.load("SpaceSoup-main/assets/images/ship-2.png")
       Surface.blit(shipSurface, self.rect)


    
    def Hit(self):
      self.health -=1