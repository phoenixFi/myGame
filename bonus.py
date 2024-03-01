# bonus.py

import pygame

class SpeedBonus(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super(SpeedBonus, self).__init__()
        self.image = pygame.image.load('images/boost.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.duration = 5  # Duration of the speed bonus in seconds
        self.vel_x = 0
        self.vel_y = 2
        self.active = False
        self.player = player
        self.spawn_time = pygame.time.get_ticks()

    def activate(self, player):
        self.active = True
        self.spawn_time = pygame.time.get_ticks()
        player.speed += 2

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.active and pygame.time.get_ticks() - self.spawn_time > self.duration * 1000:
            self.active = False

            self.player.speed -= 2

class ShieldBonus(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super(ShieldBonus, self).__init__()
        self.image = pygame.image.load('images/shield.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel_x = 0
        self.vel_y = 2
        self.duration = 5
        self.active = False
        self.spawn_time = pygame.time.get_ticks()
        self.player = player

    def activate(self):
        self.active = True
        self.spawn_time = pygame.time.get_ticks()
        self.shield_activated_time = pygame.time.get_ticks()  # Record the time of shield activation
        self.player.activate_shield()

    def update(self, player_x, player_y):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.active and pygame.time.get_ticks() - self.spawn_time > self.duration * 1000:
            self.active = False
            self.spawn_time = 0
            self.player.deactivate_shield()

class ShieldAura(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(ShieldAura, self).__init__()
        self.image = pygame.image.load('images/aura.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.duration = 10
        self.spawn_time = pygame.time.get_ticks()

    def update(self, player):
        if player.is_shielded:
            self.rect.x = player.rect.x - 150
            self.rect.y = player.rect.y -150
        if pygame.time.get_ticks() - self.spawn_time > self.duration * 1000:
            self.kill()
