import pygame
import  const as const
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super(Score, self).__init__()
        self.value = 0
        self.vont_size = 30
        self.color = (255,255,255)
        self.font = pygame.font.Font(None, self.vont_size)
        self.image = self.font.render(str(f'Score {self.value}'), False, self.color,None)
        self.rect = self.image.get_rect()
        self.rect.x = const.width - self.rect.width -20
        self.rect.y = const.height - self.rect.height -50


    def update(self):
        pass
    def update_score(self, value):
        self.value += value
        self.image = self.font.render(str(f'Score {self.value}'), False, self.color, None)
        self.rect = self.image.get_rect()
        self.rect.x = const.width - self.rect.width - 20
        self.rect.y = const.height - self.rect.height - 50