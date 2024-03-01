import time
import pygame
import random
import const as const

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super(Meteor, self).__init__()
        self.image = pygame.image.load('images/meteors/1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,const.width-self.rect.width)
        self.rect.y = -self.image.get_height()
        self.vel_x = 0
        self.vel_y = random.randrange(1,4)
        self.list = []
        self.frame_index =0
        self.anim_index=0
        self.hp = 3
        self.is_destroyed = False
        self.is_invincible = False
        self.frame_len = 3
        self.score_value = 5
        self.update_time= pygame.time.get_ticks()
        for i in range(1,65):
            img = pygame.image.load(f'images/meteors/{i}.png').convert_alpha()
            self.list.append(img)
        self.exp_list = []
        for i in range(1,8):
            img = pygame.image.load(f'images/exp/{i}.jpg').convert_alpha()
            img = pygame.transform.scale(img, (56,56))
            self.exp_list.append(img)
            self.exp_list.append(img)
            self.exp_list.append(img)

    def update(self):
        self.update_animation()
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y


    def update_animation(self):
        fps = 64
        self.image = self.list[self.frame_index]
        if self.frame_index == 63:
            self.frame_index=0
        if pygame.time.get_ticks() - self.update_time > fps:
            self.update_time = pygame.time.get_ticks()
            self.frame_index +=1
        if self.is_destroyed:
            max_index = len(self.exp_list)-1
            if self.anim_index > max_index:
                self.kill()
            else:
                self.image = self.exp_list[self.anim_index]
                self.anim_index += 1


    def get_hit(self):
        if not self.is_invincible:

            self.hp -= 1
            if self.hp <=0:
                self.is_destroyed=True
                self.is_invincible=True
                self.vel_x=0
                self.vel_y=0
                self.rect.x-=20
                self.rect.y-=20
        else:
            pass




class Spawner:
    def __init__(self):
        self.meteors_group = pygame.sprite.Group()
        self.timer = random.randrange(10, 30)

    def update(self):
        self.meteors_group.update()
        if self.timer == 0:
            self.spawn()
            self.timer = random.randrange(120,240)
        else:
            self.timer -= 1

    def spawn(self):
        new_meteor = Meteor()
        self.meteors_group.add(new_meteor)
    def meteors_clear(self):
        for meteor in self.meteors_group:
            meteor.kill()
