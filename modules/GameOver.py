import pygame

from modules import Options


def draw_text(surface, text, size, x, y):
        
        font = pygame.font.SysFont("serif", size)
        text_surface = font.render(text, True, Options.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surface.blit(text_surface, text_rect)

def show_go_screen(screen, clock, background):
    pygame.init()
    screen.blit(background,(0,0))
    draw_text(screen, "SPACESOUP", 65, Options.WIDTH//2, Options.HEIGHT//4)
    draw_text(screen, Options.INSTRUCTIONS, 27, Options.WIDTH//2, Options.HEIGHT//2)
    draw_text(screen, "Press Space To start", 20, Options.WIDTH//2, Options.HEIGHT*3/4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
              if event.key == pygame.K_SPACE:
                waiting = False

