import pygame

from modules import Options

pygame.init()
clock=pygame.time.Clock()
clock.tick(60)

class Explosion(pygame.sprite.Sprite):
	explosionFrames = []
	"""Clase que controla la animacion de la explosion"""
	def __init__(self, center):
		super().__init__()
	
		self.image = Explosion.explosionFrames[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 100 # Velocidad

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(Explosion.explosionFrames):
				self.kill() 
			else:
				center = self.rect.center
				self.image = Explosion.explosionFrames[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center