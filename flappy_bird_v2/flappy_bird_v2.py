#!/usr/bin/python
# Python 3.7
# Flappy Bird

import pygame, random, os

pygame.init()

score = 2
count = 0
dead = False

screen_height = 512
screen_width = 288

pipe_width = 52
tube1_x = 288
tube1_y = 0
tube2_x = (288 * 1.5) + (pipe_width * 0.5)
tube2_y = 0

bird_y = screen_height * 0.5
bird_x = screen_width * 0.3

screen = pygame.display.set_mode((screen_width, screen_height))
#pygame.display.caption('Flappy Bird')

bg = pygame.image.load('background-day.png').convert()
bird0 = pygame.image.load('yellowbird-downflap.png').convert()
bird1 = pygame.image.load('yellowbird-upflap.png').convert()
bird2 = pygame.image.load('yellowbird-midflap.png').convert()
pipe_greenUP = pygame.image.load('pipe-green_top.png').convert()
pipe_greenDN = pygame.image.load('pipe-green_bottom.png').convert()
pipe_redUP = pygame.image.load('pipe-red_top.png').convert()
pipe_redDN = pygame.image.load('pipe-red_bottom.png').convert()


def bird_annimation():
    global count
    if count == 0:
        screen.blit(bird0, (bird_x, bird_y))
    if count == 1:
        screen.blit(bird1, (bird_x, bird_y))
    if count == 2:
        screen.blit(bird2, (bird_x, bird_y))

    count += 1
    if count == 3:
        count = 0


run = True

font = pygame.font.SysFont('Arial', 36)


while run:

    bird_rect = pygame.draw.rect(screen, (100, 100, 100), (bird_x, bird_y, 34, 24))
    pipe_green_up_rect = pygame.draw.rect(screen, (100, 100, 100), (tube1_x, tube1_y, pipe_width, 319))
    pipe_green_dn_rect = pygame.draw.rect(screen, (100, 100, 100), (tube1_x, tube1_y + 480, pipe_width, 319))
    pipe_red_up_rect = pygame.draw.rect(screen, (100, 100, 100), (tube2_x, tube2_y, pipe_width, 319))
    pipe_red_dn_rect = pygame.draw.rect(screen, (100, 100, 100), (tube2_x, tube2_y + 480, pipe_width, 319))

    pygame.time.delay(25)
    screen.blit(bg, (0, 0))

    bird_annimation()
    screen.blit(pipe_greenUP, (tube1_x, tube1_y))
    screen.blit(pipe_greenDN, (tube1_x, tube1_y + 480))
    screen.blit(pipe_greenUP, (tube2_x, tube2_y))
    screen.blit(pipe_greenDN, (tube2_x, tube2_y + 480))

    text = font.render(str(score), True, (240, 230, 240))
    screen.blit(text, (120, 100))

    pygame.display.update()

    bird_y += 7
    tube1_x -= 2
    tube2_x -= 2
    random_num1 = random.randint(0, 284)
    random_num2 = random.randint(0, 284)

    if pygame.Rect.colliderect(bird_rect, pipe_green_up_rect) or pygame.Rect.colliderect(bird_rect,
                                                                                         pipe_green_dn_rect) or pygame.Rect.colliderect(
            bird_rect, pipe_red_up_rect) or pygame.Rect.colliderect(bird_rect, pipe_red_dn_rect):
        print('crash')
        dead = True

    while dead:
        pygame.time.delay(25)
        bird_y += 15
        screen.blit(bg, (0, 0))
        screen.blit(bird1, (bird_x, bird_y))
        screen.blit(pipe_greenUP, (tube1_x, tube1_y))
        screen.blit(pipe_greenDN, (tube1_x, tube1_y + 480))
        screen.blit(pipe_greenUP, (tube2_x, tube2_y))
        screen.blit(pipe_greenDN, (tube2_x, tube2_y + 480))
        pygame.display.update()

    if tube1_x <= 0 - pipe_width:
        tube1_x = screen_width
        tube1_y = 0 - random_num1
    if tube1_x < bird_x:
        score += 1

    if tube2_x <= 0 - pipe_width:
        tube2_x = screen_width
        tube2_y = 0 - random_num2
    if tube2_x < bird_x:
        score += 1


    if pygame.key.get_pressed()[pygame.K_SPACE]:
        bird_y -= 14
        up0 = pygame.transform.rotate(bird0, 20)
        up1 = pygame.transform.rotate(bird1, 20)
        up2 = pygame.transform.rotate(bird2, 20)
        screen.blit(up0, (bird_x, bird_y))
        screen.blit(up1, (bird_x, bird_y))
        screen.blit(up2, (bird_x, bird_y))
        pygame.display.update()

    if bird_y > screen_height:
        print('dead.')
        screen.blit(bg, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.quit()
