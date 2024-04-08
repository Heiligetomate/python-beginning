# the snake game :)))))))))
import pygame
import sys
import time as t

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000, 1000))
cube = pygame.Surface((20, 20))
cube.fill(pygame.Color('blue'))
cube1 = pygame.Surface((20, 20))
cube1.fill(pygame.Color('red'))
mouse = pygame.Surface((20, 20))
mouse.fill(pygame.Color('red'))
x_pos = 0
y_pos = 0
x1_pos = 980
y1_pos = 980
speed_cube_1 = 0.4
speed_cube_2 = 0.4
breite1 = 20
laenge1 = 20
is_moving_right = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(mouse, (mouse_pos[0], mouse_pos[1]))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x_pos = x_pos + speed_cube_1
    if keys[pygame.K_a]:
        x_pos = x_pos - speed_cube_1
    if keys[pygame.K_w]:
        y_pos = y_pos - speed_cube_1
    if keys[pygame.K_s]:
        y_pos = y_pos + speed_cube_1
    if keys[pygame.K_UP]:
        y1_pos = y1_pos - speed_cube_2
    if keys[pygame.K_DOWN]:
        y1_pos = y1_pos + speed_cube_2
    if keys[pygame.K_LEFT]:
        x1_pos = x1_pos - speed_cube_2
    if keys[pygame.K_RIGHT]:
        x1_pos = x1_pos + speed_cube_2
    if keys[pygame.K_RIGHT]:
        x1_pos = x1_pos + speed_cube_2
    if keys[pygame.K_PLUS]:
        breite1 = breite1 + 10
        laenge1 = laenge1 + 10
        cube1 = pygame.Surface((breite1, laenge1))
        speed_cube_2 = speed_cube_2 - 0.2
        t.sleep(0.5)
    if keys[pygame.K_MINUS]:
        breite1 = breite1 - 10
        laenge1 = laenge1 - 10
        cube1 = pygame.Surface((breite1, laenge1))
        speed_cube_2 = speed_cube_2 + 0.2
        t.sleep(0.5)


    screen.fill(pygame.Color('green'))
    screen.blit(cube, (x_pos, y_pos))
    screen.blit(cube1, (x1_pos, y1_pos))
    pygame.display.update()
    clock.tick(6000)

