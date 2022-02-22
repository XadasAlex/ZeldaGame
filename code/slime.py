import pygame


class Slime(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image1 = pygame.image.load('../graphics/NinjaAdventure/Enemys/slime_spr_1.png')
        self.image1 = pygame.transform.scale(self.image1, (64, 64))
        self.image2 = pygame.image.load('../graphics/NinjaAdventure/Enemys/slime_spr_2.png')
        self.image2 = pygame.transform.scale(self.image2, (64, 64))
        self.image3 = pygame.image.load('../graphics/NinjaAdventure/Enemys/slime_spr_3.png')
        self.image3 = pygame.transform.scale(self.image3, (64, 64))
        self.image4 = pygame.image.load('../graphics/NinjaAdventure/Enemys/slime_spr_4.png')
        self.image4 = pygame.transform.scale(self.image4, (64, 64))
        self.image5 = pygame.image.load('../graphics/NinjaAdventure/Enemys/slime_spr_5.png')
        self.image5 = pygame.transform.scale(self.image5, (64, 64))
        self.image6 = pygame.image.load('../graphics/NinjaAdventure/Enemys/slime_spr_6.png')
        self.image6 = pygame.transform.scale(self.image6, (64, 64))

        self.animation_list = [self.image1, self.image2, self.image3, self.image4, self.image5, self.image6, self.image5,
                               self.image4, self.image3, self.image2]
        self.animation_index = 0

        self.image = self.animation_list[self.animation_index]
        self.rect = self.image.get_rect(topleft=(0, 0))

    def animation(self):
        self.animation_index += 0.2
        self.image = self.animation_list[int(self.animation_index)]

        if self.animation_index >= 9.5:
            self.animation_index = 0

    def update(self):
        self.animation()