import pygame
from pygame.locals import *
import time
from sys import exit
from gameobjects.vector2 import Vector2
from math import *
import random



class HeroPlane(object):
    def __init__(self, screen_temp):
        self.screen = screen_temp
        self.x = 0
        self.y = 200
        self.image = pygame.image.load("./image/myplane.gif").convert_alpha()
        self.pos = Vector2(self.x, self.y)
        self.speed = 300
        self.rotation = 1
        self.rotationspeed = 360
        self.rotationHeroplane = pygame.transform.rotate(self.image, self.rotation)
        self.w, self.h = self.rotationHeroplane.get_size()
        self.draw_pos = Vector2(self.pos.x - self.w / 2, self.pos.y - self.h / 2)

    def moveleft(self):
        print('left')
        self.draw_pos.x -= 3

    def moveright(self):
        print('right')
        self.draw_pos.x += 3

    def moveup(self):
        print('up')
        self.draw_pos.y -= 3

    def movedown(self):
        print('down')
        self.draw_pos.y += 3

    def dispaly(self):
        self.screen.blit(self.rotationHeroplane, self.draw_pos)

class bullet(object):
    def __init__(self, screen_temp):
        self.screen = screen_temp
        self.x = HeroPlane.draw_pos.x
        self.y = 200
        self.image = pygame.image.load("./image/myplane.gif").convert_alpha()

def keyControl(HeroPlane):
    for event in pygame.event.get():
        if event.type == QUIT:
            print('quit')
            exit()

    key = pygame.key.get_pressed()
    keys_lu = pygame.key.set_mods(K_LEFT | K_UP)

    rotation_dirction = 0
    movement_dirction = 0

    if key[K_LEFT] or key[K_a]:
        rotation_dirction = +1
        HeroPlane.moveleft()
    elif key[K_RIGHT] or key[K_d]:
        rotation_dirction = -1
        HeroPlane.moveright()
    elif key[K_DOWN] or key[K_s]:
        movement_dirction = -1
        HeroPlane.movedown()
    elif key[K_UP] or key[K_w]:
        movement_dirction = +1
        HeroPlane.moveup()
    elif keys_lu:
        print('keys_lu')
        HeroPlane.pos.y -= 0.5
        HeroPlane.pos.x -= 0.5
    clock = pygame.time.Clock()
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    HeroPlane.rotation += rotation_dirction * HeroPlane.rotationspeed * time_passed_seconds

    # 获得前进（x方向和y方向）
    heading_x = sin(HeroPlane.rotation * pi / 180.)
    heading_y = cos(HeroPlane.rotation * pi / 180.)
    # 转换为单位速度向量
    heading = Vector2(heading_x, heading_y)
    # 转换为速度
    heading *= movement_dirction

    HeroPlane.pos += heading * HeroPlane.speed * time_passed_seconds

    if HeroPlane.draw_pos.x < 0:
        HeroPlane.draw_pos.x = 0
    elif HeroPlane.draw_pos.x > 690:
        HeroPlane.draw_pos.x = 690

    elif HeroPlane.draw_pos.y < 0:
        HeroPlane.draw_pos.y = 0#
    elif HeroPlane.draw_pos.y > 402:
        HeroPlane.draw_pos.y = 402

def main():
    # make a window
    screen = pygame.display.set_mode((800, 450), 0, 0, 0)

    # paste a picture on backgroud
    backgroud = pygame.image.load("./image/backgroud.jpg").convert()

    # paste a pic on my airplane
    Hero = HeroPlane(screen)
    clock = pygame.time.Clock()

    # paste a cloud in air
    cloud = pygame.image.load('./image/cloud.png').convert_alpha()

    cloud_x = 800
    cloud_y = random.randint(45, 300)
    random_size = random.uniform(0.3,1.0)
    cloud_speed = int(10*random_size)-4

    while True:
        keyControl(Hero)
        screen.blit(backgroud, (0, 0))
        tempNum=random_size
        cloud = pygame.transform.smoothscale(cloud,(int(562*tempNum),int(432*tempNum)))
        screen.blit(cloud, (cloud_x, cloud_y))
        Hero.dispaly()

        if cloud_speed>0:
            cloud_x -= cloud_speed
        else:
            cloud_x -=1

        pygame.display.update()
        time.sleep(0.01)

if __name__ == "__main__":
    main()
