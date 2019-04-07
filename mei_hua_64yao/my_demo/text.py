import pygame
from pygame.locals import *
import time
from sys import exit
from gameobjects.vector2 import Vector2
from math import *
import random


class Backgroud(object):
    def __init__(self, screen_temp):
        #self.cloud_x=800
        #self.cloud_y=random.randint(45, 300)
        self.screen = screen_temp
        self.image = pygame.image.load("./image/backgroud.jpg").convert()
        self.cloud = Cloud(screen_temp)
        self.cloud_list = []

    def display(self):
        self.screen.blit(self.image, (0, 0))
        i = random.randint(1,100)
        if i == 40 or i == 50:
            self.cloud_list.append(self.cloud)

        for cloud_i in self.cloud_list:
             cloud_i.display()
             cloud_i.move()
             if cloud_i.judge():
                 self.cloud_list.remove(cloud_i)





class HeroPlane(object):
    def __init__(self, screen_temp):
        self.screen = screen_temp
        self.x = 0
        self.y = 200
        self.image = pygame.image.load('./image/myplane.gif')
        self.Herobullet = Bullet(screen_temp, self.x, self .y)
        self.bullet_list = [Bullet(self.screen,self.x,self.y)]*10

    def moveleft(self):
        print('left     %d' % self.x)
        self.x -= 3

    def moveright(self):
        print('right    %d' % self.x)
        self.x += 3

    def moveup(self):
        print('up   %d' % self.y)
        self.y -= 3

    def movedown(self):
        print('down     %d' % self.y)
        self.y += 3

    def fire(self):
        print('fire  x=%d   y=%d' % (self.x, self.y))
        print(self.bullet_list)
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

    def dispaly(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullettemp in self.bullet_list:
            bullettemp.dispaly()
            bullettemp.move()
            if bullettemp.judge():
                self.bullet_list.remove(bullettemp)

class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.screen = screen_temp
        self.x = x + 70 - 8
        self.y = y + 15
        self.image = pygame.image.load("./image/bullet_7.png")

    def dispaly(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.x += 10


    def judge(self):
        if self.x > 850:
            return True
        else:
            return False


class Cloud(object):
    def __init__(self, screen_temp):
        self.screen = screen_temp
        self.x = 800
        self.y = 45
        self.image = pygame.image.load('./image/cloud.png').convert_alpha()
        self.random_size = random.uniform(0.5, 0.7)
        self.cloud_speed = int(10 * self.random_size) - 4
        self.tempNum = self.random_size
        self.transform = pygame.transform.smoothscale(self.image, (int(562 * self.tempNum), int(432 * self.tempNum)))
        self.cloud_list = []

    def display(self):
        self.y = random.randint(45,200)
        self.screen.blit(self.transform, (self.x, self.y))
        print('cloud be display')

    def move(self):
        self.x -= self.cloud_speed
        print('cloud x=%d  y=%d'%(self.x,self.y))

    def judge(self):
        if self.x < -570:
            return True
        else:
            return False


def keyControl(HeroPlane):
    for event in pygame.event.get():
        if event.type == QUIT:
            print('quit')
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                HeroPlane.fire()

    key = pygame.key.get_pressed()

    if key[K_LEFT] or key[K_a]:
        HeroPlane.moveleft()
    elif key[K_RIGHT] or key[K_d]:
        HeroPlane.moveright()
    elif key[K_DOWN] or key[K_s]:
        HeroPlane.movedown()
    elif key[K_UP] or key[K_w]:
        HeroPlane.moveup()
    #elif key[K_SPACE]:
    #    HeroPlane.fire()


    if HeroPlane.x < 0:
        HeroPlane.x = 0
    elif HeroPlane.x > 690:
        HeroPlane.x = 690

    elif HeroPlane.y < 0:
        HeroPlane.y = 0  #
    elif HeroPlane.y > 402:
        HeroPlane.y = 402


def main():
    screen = pygame.display.set_mode((800, 450), 0, 0, 0)
    backgroud = Backgroud(screen)
    hero = HeroPlane(screen)
    while True:
        keyControl(hero)
        backgroud.display()
        hero.dispaly()
        pygame.display.update()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
