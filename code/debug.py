import pygame

pygame.init()
font = pygame.font.Font(None, 30)


def debug(info, y=10, x=10):
    display_surface = pygame.display.get_surface()
    debug_surface = font.render(str(info), True, 'white')
    debug_rect = debug_surface.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surface, debug_rect)


def show_fps(fps, x=10, y=35):
    display_surface = pygame.display.get_surface()
    debug_surface = font.render('FPS: ' + str(int(fps)), True, 'white')
    debug_rect = debug_surface.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surface, debug_rect)

# todo: write function here that loads image and scales it according to a scaling factor


