import pygame
import const as const
from bullet import Bullet
from hud import HUD
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.is_shielded = False
        self.shield_activation_time = 0
        self.image = pygame.image.load('images/Daco_4889272.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = const.width//2
        self.rect.y = const.height - 140
        self.bullets = pygame.sprite.Group()
        self.snd_damage = pygame.mixer.Sound('images/23 Damage.mp3')
        self.snd_shoot = pygame.mixer.Sound('13 Fighter Shot1.mp3')
        self.hud = HUD()
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.hp = 5
        self.alive = True
    def update(self):
        self.bullets.update()
        self.hud_group.update()


        for bullet in self.bullets:
            if bullet.rect.y <=0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x <=0:
            self.rect.x = 0
        elif self.rect.x >= const.width - self.rect.width:
            self.rect.x = const.width - self.rect.width
        self.rect.y += self.vel_y
        if self.rect.y >= const.height-self.rect.height-100:
            self.rect.y = const.height - self.rect.height-100

    def activate_shield(self):
        self.is_shielded = True
        self.shield_activation_time = pygame.time.get_ticks()

    def deactivate_shield(self):
        self.is_shielded = False

    def shoot(self):
        self.snd_shoot.play()
        new_bullet = Bullet()
        new_bullet.rect.x = self.rect.x + self.rect.width//2
        new_bullet.rect.y = self.rect.y
        self.bullets.add(new_bullet)

    def get_hit(self):
        self.snd_damage.play()
        self.hp -= 1
        self.hud.health_bar.hp_value()
        if self.hp <= 0:
            self.alive = False



    def game_over(self):
        print("Game Over")
