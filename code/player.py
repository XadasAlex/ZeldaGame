import pygame
from settings import *

# useless comment
# ohhhhhh maxx
# I made some important changes to the project
# sheesh
# sheesh maaaax

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups):
		super().__init__(groups)
		self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft=pos)

		self.direction = pygame.math.Vector2D()

	def input(self):
		keys = pygame.key.get_pressed()