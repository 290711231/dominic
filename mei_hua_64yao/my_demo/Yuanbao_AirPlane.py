import sys
from Plane import *
from Backgroud import *
from KeyInput import *

def main():
    screen = pygame.display.set_mode((800, 555), 0, 0, 0)
    backgroud = Backgroud(screen)
    enemy = EnemyPlane(screen)
    hero = HeroPlane(screen)
    clock = pygame.time.Clock()
    while True:
        clock.tick(100)
        keyControl(hero)
        backgroud.display()
        hero.dispaly()
        #hero.animate()
        enemy.move()
        # enemy.dispaly()
        pygame.display.update()
        #time.sleep(0.01)


if __name__ == "__main__":
    main()
