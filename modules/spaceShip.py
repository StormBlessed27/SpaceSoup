import pygame

from modules import options

class spaceShip(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(options.SHIP_IMAGE).convert()
        self.image.set_colorkey("BLACK")
        self.rect = self.image.get_rect()
        self.rect.centerx = options.WIDTH//2
        self.rect.bottom=options.HEIGHT-10
        self.speed = options.SPEED

    def Move(self):
        teclas_pres = pygame.key.get_pressed()
        if teclas_pres[pygame.K_d] or teclas_pres[pygame.K_RIGHT]:
           self.rect.x += self.speed 
        elif teclas_pres[pygame.K_a] or teclas_pres[pygame.K_LEFT]:
          self.rect.x -= self.speed

        if teclas_pres[pygame.K_s] or teclas_pres[pygame.K_DOWN]:
           self.rect.y += self.speed
        elif teclas_pres[pygame.K_w] or teclas_pres[pygame.K_UP]:
          self.rect.y -= self.speed
