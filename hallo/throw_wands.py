import pygame
import sys
import time as t

pygame.init()

x = 1000
y = 1000
clock = pygame.time.Clock()
bg = pygame.image.load("backround.png")
tomatoe = pygame.image.load("tomatoe.png")
apple = pygame.image.load("apple_small.png")
screen = pygame.display.set_mode((x, y))
cube = pygame.Surface((50, 50))

man = pygame.Surface((20, 20))


x_pos_man = y / 2
y_pos_man = x / 2
moving_up = True
moving_left = False
moving_right = False
moving_down = False
speed = 5

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(bg, (0, 0))
    screen.blit(apple, (100, 100))
    screen.blit(cube, (x_pos_man, y_pos_man))

    keys = pygame.key.get_pressed()
    if moving_up == True:
        y_pos_man -= speed
    if moving_down == True:
        y_pos_man += speed
    if moving_left == True:
        x_pos_man -= speed
    if moving_right == True:
        x_pos_man += speed
    if keys[pygame.K_a]:
        moving_left = True
        moving_right = False
        moving_up = False
        moving_down = False
    if keys[pygame.K_d]:
        moving_left = False
        moving_right = True
        moving_up = False
        moving_down = False
    if keys[pygame.K_w]:
        moving_left = False
        moving_right = False
        moving_up = True
        moving_down = False
    if keys[pygame.K_s]:
        moving_left = False
        moving_right = False
        moving_up = False
        moving_down = True

    if y_pos_man < 0:
        y_pos_man = 1000 - man.get_height()
    if y_pos_man > 1000:
        y_pos_man = 0 + man.get_height()
    if x_pos_man < 0:
        x_pos_man = 1000 - man.get_height()
    if x_pos_man > 1000:
        x_pos_man = 0 + man.get_height()


        #y_pos_man += 20

    pygame.display.update()
    clock.tick(60)
    screen.fill(("Red"))