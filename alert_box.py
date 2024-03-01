import pygame
import const as const

class AlertBox(pygame.sprite.Sprite):
    def __init__(self):
        super(AlertBox, self).__init__()
        self.font = pygame.font.Font(None,50)
        self.color = (255,0 , 0)
        self.message = "GAME OVER"
        self.image = self.font.render(self.message,0,self.color)
        self.rect = self.image.get_rect()
        self.rect.x = const.width//2 - self.rect.width//2
        self.rect.y = const.height//2 - self.rect.height//2
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y