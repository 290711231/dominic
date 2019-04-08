#!/usr/bin/env python
# -*- coding:utf-8 -*-

from Bullet import *



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

