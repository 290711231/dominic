import pygame
from pygame.locals import *
import time
from sys import exit
from gameobjects.vector2 import Vector2
from math import *
import random


def main():
    # make a window
    screen = pygame.display.set_mode((800, 450), 0, 0, 0)

    # paste a picture on backgroud
    backgroud = pygame.image.load("./image/backgroud.jpg").convert()

    # paste a pic on my airplane
    HeroPlane = pygame.image.load("./image/myplane.gif").convert_alpha()
    clock = pygame.time.Clock()

    #paste a cloud in air
    cloud =pygame.image.load('./image/cloud.png').convert_alpha()

    x = 0
    y = 200
    pos = Vector2(x, y)
    speed = 300
    rotation = 0
    rotationspeed = 360

    cloud_x = 800
    cloud_y = random.randint(45,300)
    random_size = random.uniform(0.3,1.0)
    cloud_speed = random.randint(1,3)



    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                print('quit')
                exit()

        key = pygame.key.get_pressed()
        keys_lu = pygame.key.set_mods(K_LEFT|K_UP)

        rotation_dirction = 0
        movement_dirction = 0

        if key[K_LEFT] or key[K_a]:
            print('left')
            rotation_dirction -= 15
            pos.x -= 3
        elif key[K_RIGHT] or key[K_d]:
            print('right')
            rotation_dirction += 30
            pos.x += 3
        elif key[K_DOWN] or key[K_s]:
            print('down')
            #movement_dirction += 5
            pos.y += 3
        elif key[K_UP] or key[K_w]:
            print('up')
            #movement_dirction -= 5
            pos.y -= 3
        elif keys_lu:
            print('keys_lu')
            pos.y -= 0.5
            pos.x -= 0.5


        screen.blit(backgroud, (0, 0))
        #cloud = pygame.transform.smoothscale(cloud,(int(562*(1-random_size)),int(432*(1-random_size))))
        screen.blit(cloud,(cloud_x,cloud_y))
        rotationHeroplane = pygame.transform.rotate(HeroPlane, rotation)
        w, h = rotationHeroplane.get_size()
        draw_pos = Vector2(pos.x - w / 2, pos.y - h / 2)
        screen.blit(rotationHeroplane, draw_pos)


        cloud_x -= cloud_speed

        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.0

        time_passed = clock.tick()
        time_passed_seconds = time_passed / 1000.0

        # 图片的转向速度也需要和行进速度一样，通过时间来控制
        rotation += rotation_dirction * rotationspeed * time_passed_seconds

        # 获得前进（x方向和y方向），这两个需要一点点三角的知识
        heading_x = sin(rotation * pi / 180.)
        heading_y = cos(rotation * pi / 180.)
        # 转换为单位速度向量
        heading = Vector2(heading_x, heading_y)
        # 转换为速度
        heading *= movement_dirction

        pos += heading * speed * time_passed_seconds

        if pos.x<0:
            pos.x = 0
        elif pos.x>690:
            pos.x=690

        elif pos.y<0:
            pos.y=0
        elif pos.y>402:
            pos.y =402


        pygame.display.update()



        time.sleep(0.01)


if __name__ == "__main__":
    main()
