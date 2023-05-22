import pygame

from modules import Options

class Score(pygame.sprite.Sprite):

    def draw_text(surface, text, size, x, y):
        font = pygame.font.SysFont("serif", size)
        text_surface = font.render(text, True, Options.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)