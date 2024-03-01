import pygame
import const as const
from score import Score
class HUD(pygame.sprite.Sprite):
    def __init__(self):
        super(HUD, self).__init__()
        self.image = pygame.image.load('images/hudi4.png').convert()
        self.image = pygame.transform.scale(self.image, (const.width, 70))
        self.rect = self.image.get_rect()
        self.rect.y = const.height - self.rect.height-50
        self.health_bar = Health_bar()
        self.health_bar.rect.x = 10
        self.health_bar.rect.y = const.height - self.health_bar.rect.height-28
        self.health_bar_group = pygame.sprite.Group()
        self.health_bar_group.add(self.health_bar)
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.score = Score()
        self.score_group = pygame.sprite.Group()
        self.score_group.add(self.score)
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        self.score_group.update()




class Health_bar(pygame.sprite.Sprite):
    def __init__(self,hp=5):
        super(Health_bar, self).__init__()
        self.max_hp =hp
        self.hp = self.max_hp
        self.image = pygame.image.load('images/health/1.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 40))
        self.image_list = []
        self.index = 0
        for i in range(2,5):
            image = pygame.image.load(f'images/health/{i}.jpg').convert_alpha()
            image = pygame.transform.scale(image, (150, 40))
            self.image_list.append(image)
        self.rect = self.image.get_rect()

        self.rect.y = const.height - self.rect.height
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def hp_value(self):
        self.hp -= 1
        if self.index < len(self.image_list):
            self.image = self.image_list[self.index]
            self.index += 1
        else:
            self.index = 0