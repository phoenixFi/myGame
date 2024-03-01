import pygame
import random
import const as const
from ship import Ship
from background import Bg
from meteors import Spawner
from particles import ParticleSpawner
from alert_box import AlertBox
from bonus import ShieldBonus, SpeedBonus, ShieldAura
pygame.init()
pygame.mixer.init()
display = pygame.display.set_mode((const.width,const.height))

fps = 60
clock = pygame.time.Clock()
pygame.display.set_caption("Endterm Project")
icon = pygame.image.load('images/icon3.png')
pygame.display.set_icon(icon)

bg = Bg()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
speed_bonuses = pygame.sprite.Group()
shield_bonuses = pygame.sprite.Group()
meteor_spawn = Spawner()
particle_spawn = ParticleSpawner()
all_sprites = pygame.sprite.Group()
shield_auras = pygame.sprite.Group()
alert_box_group = pygame.sprite.Group()

pygame.mixer.music.load('01. Zone 1 - Asteroid Zone.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=True)
running =True
while running:
    #Tick
    clock.tick(fps)

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.vel_x = -player.speed
            elif event.key == pygame.K_d:
                player.vel_x = player.speed
            elif event.key == pygame.K_w:
                player.vel_y = -player.speed
            elif event.key == pygame.K_s:
                player.vel_y = player.speed
            if event.key == pygame.K_SPACE:
                player.shoot()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.vel_x = 0
            elif event.key == pygame.K_d:
                player.vel_x = 0
            elif event.key == pygame.K_w:
                player.vel_y = 0
            elif event.key == pygame.K_s:
                player.vel_y = 0


    #update
    bg_group.update()
    sprite_group.update()
    meteor_spawn.update()
    particle_spawn.update()

    speed_bonus_collisions = pygame.sprite.spritecollide(player, speed_bonuses, True)
    for speed_bonus in speed_bonus_collisions:
        speed_bonus.activate(player)

    shield_bonus_collisions = pygame.sprite.spritecollide(player, shield_bonuses, True)
    for shield_bonus in shield_bonus_collisions:
        shield_bonus.activate()
        player.activate_shield()
        shield_aura = ShieldAura(player.rect.x -player.rect.x, player.rect.y - player.rect.y)
        shield_auras.add(shield_aura)


    collided = pygame.sprite.groupcollide(player.bullets, meteor_spawn.meteors_group, True, False)
    for bullet, meteor in collided.items():
        meteor[0].get_hit()
        player.hud.score.update_score(meteor[0].score_value)
        if not meteor[0].is_invincible:
            particle_spawn.particleSpawn(bullet.rect.x, bullet.rect.y)
    if not player.is_shielded:
        collided = pygame.sprite.spritecollide(player, meteor_spawn.meteors_group, False)
        for meteor in collided:
            if not meteor.is_invincible:
                player.get_hit()
            meteor.hp=0
            meteor.get_hit()




    if random.randint(1, 900) == 1:
        speed_bonus = SpeedBonus(random.randint(0, const.width - 30), 0,player)
        speed_bonuses.add(speed_bonus)

    if random.randint(1, 900) == 1:
        shield_bonus = ShieldBonus(random.randint(0, const.width - 30), 0, player)
        shield_bonuses.add(shield_bonus)


    #for i in shield_auras:
        #i.update(player)
    speed_bonuses.update()
    shield_bonuses.update(player.rect.x , player.rect.y )

    shield_auras.update(player)
    all_sprites.update()


    if not player.alive:
        meteor_spawn.meteors_clear()
        alert_box = AlertBox()
        alert_box_group.add(alert_box)
        player.kill()


    #render display
    display.fill((0,0,0))
    bg_group.draw(display)



    meteor_spawn.meteors_group.draw(display)
    player.bullets.draw(display)
    particle_spawn.particle_group.draw(display)
    speed_bonuses.draw(display)
    shield_auras.draw(display)
    player.hud_group.draw(display)
    player.hud.health_bar_group.draw(display)
    shield_bonuses.draw(display)
    sprite_group.draw(display)
    player.hud.score_group.draw(display)
    all_sprites.draw(display)
    alert_box_group.draw(display)


    pygame.display.update()

