import pygame
from modules import Opciones

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load(Opciones.BULLET_IMG)
        self.image.set_colorkey("BLACK")
        self.rect=self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -5

    def Move(self):
        self.rect.y +=self.speedy
        if self.rect.bottom<0:
            self.kill()

            