import pygame
class spaceShip:
    '''Create the player SpaceShip'''

    def __init__(self, x:int, y:int, shipSpeed:int) -> None:
        self.rect = pygame.Rect(x,y, 2,2)
        self.shipSpeed = shipSpeed
        self.health = 4

    def Move(self):
        teclas_pres = pygame.key.get_pressed()

        if teclas_pres[pygame.K_d]:
          self.rect.x += self.shipSpeed
        elif teclas_pres[pygame.K_a]:
          self.rect.x -= self.shipSpeed

        if teclas_pres[pygame.K_s]:
          self.rect.y += self.shipSpeed
        elif teclas_pres[pygame.K_w]:
          self.rect.y -= self.shipSpeed

    def Shoot():
        algotambien = 0

    def Draw(self, Surface: pygame.Surface):
      shipSurface = pygame.Surface((5,5))
      shipSurface.fill('Green')
      Surface.blit(shipSurface, self.rect)
    
    def Hit(self):
      self.health -=1