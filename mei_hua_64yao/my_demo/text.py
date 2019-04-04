import pygame
from pygame.locals import *
import time
from sys import exit
from gameobjects.vector2 import Vector2
from math import *
import random

def main():
    animationnum = 0
    for a in range(70):
        if a % 10 == 0:
            animationnum += 1
            image = pygame.image.load("./image/bullet_%d.png" % animationnum)
        elif a == 70:
            image = pygame.image.load("./image/bullet_7.png")

    while True:
        screen = pygame.display.set_mode((800, 450), 0, 0, 0)
        backgroud = pygame.image.load("./image/backgroud.jpg").convert()
        screen.blit(backgroud, (0, 0))
        screen.blit(image, (200, 200))




if __name__ == "__main__":
    main()