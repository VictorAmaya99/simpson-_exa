import pygame
import sys
import random

from donas import Dona
from config import *

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Donuts War")

icono = pygame.image.load("./src/images/dona.png").convert_alpha()
icono = pygame.transform.scale(icono, SIZE_ICON)
pygame.display.set_icon(icono)

font = pygame.font.Font("./src/fonts/Simpson.ttf", 48)

score = 0

sonido = pygame.mixer.Sound("./src/sounds/ouch.mp3")
pygame.mixer.music.load("./src/sounds/ouch.mp3")
flag_sonido = True

fondo = pygame.image.load("./src/images/background.jpg").convert()
fondo = pygame.transform.scale(fondo, SIZE)

donas = []
for i in range(10):
    x = random.randrange(30, WIDTH - 30)
    y = random.randrange(-1000, 0) 

    dona = Dona(DONUT_SIZE, (x, y), "./src/images/dona.png") 

    # dona = pygame.image.load("./src/images/dona.png").convert_alpha()
    # dona = pygame.transform.scale(dona, DONUT_SIZE)
    # dona.get_rect().center = (x, y)
    # print(dona.get_rect().center)
    donas.append(dona)


homero_l = pygame.image.load("./src/images/homer_left.png").convert_alpha()
homero_l = pygame.transform.scale(homero_l, HOMER_SIZE)
homero_r = pygame.image.load("./src/images/homer_right.png").convert_alpha()
homero_r = pygame.transform.scale(homero_r, HOMER_SIZE)
homero = homero_l
rect_homero = homero_l.get_rect()
rect_homero.midbottom = (CENTER_X, DISPLAY_BOTTOM)
rect_boca = pygame.rect.Rect(0, 0, 50, 10)
rect_boca.x = rect_homero.x + 40
rect_boca.y = rect_homero.y + 130





# rect_homero = homero_r.get_rect()
# rect_homero.midbottom = (CENTER_X, DISPLAY_BOTTOM)


while True:
    
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    

    if keys [pygame.K_LEFT]:
        if rect_homero.left > DISPLAY_LEFT:
            rect_homero.x -= HOMER_SPEED
            rect_boca.x = rect_homero.x + 40
            rect_boca.y = rect_homero.y + 130
            homero = homero_l

    if keys [pygame.K_RIGHT]:
        if rect_homero.right < DISPLAY_RIGTH:
            rect_homero.x += HOMER_SPEED
            rect_boca.x = rect_homero.x + 70
            rect_boca.y = rect_homero.y + 130
            homero = homero_r

    screen.blit(fondo, ORIGIN)

    texto = font.render("Score: " + str(score), True, GREEN)
    screen.blit(texto, SCORE_POS)

    pygame.draw.rect(screen, RED, rect_boca )
    screen.blit(homero, rect_homero)

    for dona in donas:

        if dona.rect.bottom < DISPLAY_BOTTOM:
            flag_dona = True
            flag_sonido = True
            if dona.active:
                dona.update()
            else:
                dona.rect.y = 0

            if rect_boca.colliderect(dona.rect):
                
                dona.active = False
                if flag_sonido:
                    score += 1
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_pos(0.3)
                    flag_sonido = False
                else:
                    flag_sonido = True
    
            if dona.active:
                screen.blit(dona.image, dona.rect)

    pygame.display.flip()