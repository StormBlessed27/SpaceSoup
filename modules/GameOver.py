import pygame

from modules import Options

screen = pygame.display.set_mode((Options.WIDTH, Options.HEIGHT))
gameClock = pygame.time.Clock()

def show_go_screen(draw_text):
    draw_text(screen, "SPACESOUP", 65, Options.WIDTH//2, Options.HEIGHT//4)
    draw_text(screen, "Instrucciones van aquí", 27, Options.WIDTH//2, Options.HEIGHT//2)
    draw_text(screen, "Press Key", 20, Options.WIDTH//2, Options.HEIGHT*3/4)
    pygame.display.flip()
    waiting = True
    
    while waiting:
        gameClock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

