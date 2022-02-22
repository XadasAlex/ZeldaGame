import pygame, sys
from settings import *
from level import Level
from debug import *
from slime import *


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()
        self.level = Level()

        # experimental slime
        self.slime = pygame.sprite.GroupSingle()
        self.slime.add(Slime())


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')

            # experimental slime
            self.slime.draw(self.screen)
            self.slime.update()
            self.level.run()

            # draw current fps
            # show_fps(self.clock.get_fps())
            pygame.display.update()

            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
