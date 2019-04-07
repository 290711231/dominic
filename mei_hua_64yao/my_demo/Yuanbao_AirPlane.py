import pygame
from pygame.locals import *
import time
from sys import exit
from gameobjects.vector2 import Vector2
from math import *
import random


class Backgroud(object):
    def __init__(self, screen_temp):
        self.cloud_x = 800
        self.cloud_y = random.randrange(80,160)
        self.screen = screen_temp
        self.image = pygame.image.load("./image/backgroud.jpg").convert()
        self.bgimage_1 = BackgroudImage(self.screen,'backgroud_1',0,238,1)
        self.bgimage_2 = BackgroudImage(self.screen,'backgroud_2',0,0,0.3)
        self.cloud = Cloud(screen_temp, self.cloud_x, self.cloud_y)
        self.cloud_list = []
        self.backgroudlist_1 = []
        self.backgroudlist_2 = []


    def display(self):
        #载入背景
        self.screen.blit(self.image, (0, 0))
        #self.screen.blit(self.bgimage_1.image,(0,47))
        #self.bgimage_1.move()

        #载入后面的天空
        self.backgroudlist_2.append(BackgroudImage(self.screen,'backgroud_2',1020,0,0.3))
        #elif len(self.backgroudlist_2)==1:
        #    self.backgroudlist_2.append(BackgroudImage(self.screen, 'backgroud_2', 0, 0, 0.3))
        self.bgimage_2.display()
        self.bgimage_2.move()
        self.bgimage_2.judge()

        #for baimage2 in self.backgroudlist_2:
        #    baimage2.display()
        #    baimage2.move()
        #    baimage2.judge()


        #载入天空中的云
        i = random.randrange(1, 300)
        if i == 40 or i == 80 or i == 120:
            self.cloud_list.append(Cloud(self.screen, self.cloud_x, self.cloud_y))

        for cloud_i in self.cloud_list:
            cloud_i.display()
            cloud_i.move()
            if cloud_i.judge():
                self.cloud_list.remove(cloud_i)
                print('____________cloud be remove____________')

        #载入后面的大树背景
        self.bgimage_1.display()
        self.bgimage_1.move()

class BackgroudImage(object):
    def __init__(self, screen_temp,temp_image,temp_x,temp_y,temp_speed):
        self.screen = screen_temp
        self.bgimage = temp_image
        self.x = temp_x
        self.y = temp_y
        self.image = pygame.image.load('./image/%s.png'%self.bgimage).convert_alpha()
        self.speed = temp_speed

    def display(self):

        self.screen.blit(self.image, (self.x, self.y))
        self.screen.blit(self.image,(self.x+510,self.y))

        print('%s be display'%self.bgimage)

    def move(self):
        self.x -= self.speed
        #print('now x is %d'%self.x)

    def judge(self):
        #判断越界
        if self.x < -510:
            return True
        else:
            return False

class HeroPlane(object):
    def __init__(self, screen_temp):
        self.screen = screen_temp
        self.x = 0
        self.y = 200
        self.image = pygame.image.load('./image/myplane-1.png')
        self.Herobullet = Bullet(screen_temp, self.x, self.y)
        self.bullet_list = [Bullet(self.screen, self.x, self.y)] * 10

    #def animate(self):
    #    rangenum(22)
    #    self.image =pygame.image.load('./image/myplane-%d.png'%self.image_temp)

    def moveleft(self):
        print('left     %d' % self.x)
        self.x -= 5

    def moveright(self):
        #print('right    %d' % self.x)
        self.x += 5

    def moveup(self):
        #print('up   %d' % self.y)
        self.y -= 5

    def movedown(self):
        #print('down     %d' % self.y)
        self.y += 5

    def fire(self):
        #开火
        #print('fire  x=%d   y=%d' % (self.x, self.y))
        #print(self.bullet_list)
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

    def dispaly(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullettemp in self.bullet_list:
            bullettemp.dispaly()
            bullettemp.move()
            if bullettemp.judge():
                self.bullet_list.remove(bullettemp)

class EnemyPlane(object):
    def __init__(self, screen_temp):
        self.screen = screen_temp
        self.x = 800
        self.y = random.randrange(50,450)
        self.image = pygame.image.load('./image/enemy_1_1.png')
        self.enemybullet = Bullet(screen_temp, self.x, self.y)
        self.enemybullet_list = [Bullet(self.screen, self.x, self.y)] * 10
        self.speed = random.uniform(0.8,1.2)

    def move(self):
        self.x -= self.speed

    def fire(self):
        for enemybulletnum in random.randrange(1,200):
            if enemybulletnum == 40 or enemybulletnum == 50:
                #print('enemy fire  x=%d   y=%d' % (self.x-66, self.y+44))
                #print(self.enemybullet_list)
                self.enemybullet_list.append(Bullet(self.screen, self.x, self.y))

    def dispaly(self):
        self.screen.blit(self.image, (self.x, self.y))
        for add_enemybulletnum in range(1,501):
            if add_enemybulletnum%50 == 0:
                for bullettemp in self.enemybullet_list:
                    bullettemp.dispaly()
                    bullettemp.enemymove()
                    if bullettemp.enemyjudge():
                        self.enemybullet_list.remove(bullettemp)


class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.screen = screen_temp
        self.x = x + 70 - 8
        self.y = y + 15
        self.image = pygame.image.load("./image/bullet_7.png")
        self.enemyimage = pygame.image.load('./image/bullet_2.png')

    def dispaly(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        #英雄的子弹移动
        self.x += 10

    def enemymove(self):
        #敌人的子弹移动
        self.x -= 10

    def judge(self):
        #判断英雄的子弹越界
        if self.x > 850:
            return True
        else:
            return False

    def enemyjudge(self):
        #判断敌人的子弹越界
        if self.x < -50:
            return True
        else:
            return False


class Cloud(object):
    def __init__(self, screen_temp, x, y):
        self.screen = screen_temp
        self.x = x
        self.y = y
        self.cloudnum = random.randrange(1,4)
        self.image = pygame.image.load('./image/cloud-%d.png'%self.cloudnum).convert_alpha()
        self.random_size = random.uniform(0.4, 0.7)
        self.cloud_speed = 10-int(10 * self.random_size) - 2
        self.tempNum = self.random_size
        self.transform = pygame.transform.smoothscale(self.image, (int(562 * self.tempNum), int(432 * self.tempNum)))
        self.cloud_list = []

    def display(self):
        self.screen.blit(self.transform, (self.x, self.y))
        #print('cloud be display')

    def move(self):
        self.x -= self.cloud_speed
        #print('cloud x=%d  y=%d' % (self.x, self.y))

    def judge(self):
        #判断云的越界
        if self.x < -360:
            return True
        else:
            return False

def keyControl(HeroPlane):
    #键盘控制
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
    # elif key[K_SPACE]:
    #    HeroPlane.fire()

    if HeroPlane.x < 0:
        HeroPlane.x = 0
    elif HeroPlane.x > 690:
        HeroPlane.x = 690

    elif HeroPlane.y < 0:
        HeroPlane.y = 0  #
    elif HeroPlane.y > 450:
        HeroPlane.y = 450


def main():
    screen = pygame.display.set_mode((800, 555), 0, 0, 0)
    backgroud = Backgroud(screen)
    enemy = EnemyPlane(screen)
    hero = HeroPlane(screen)
    clock = pygame.time.Clock()
    i = 0
    while True:
        clock.tick(100)
        i += 1
        keyControl(hero)
        backgroud.display()
        hero.dispaly()
        #hero.animate()
        enemy.dispaly()
        enemy.move()
        pygame.display.update()
        #time.sleep(0.01)


if __name__ == "__main__":
    main()
