import sys
import numpy as np
import pygame
from time import sleep
import os
import pygame.freetype
pygame.init()


size = width, height = 1000, 800
speed = [1, 1]
black = 60, 60, 60
BLACK=(0,0,0)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 

screen = pygame.display.set_mode(size)

player1_score = 0
player2_score = 0

pygame.font.init()
font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"fonts","SourceSansPro-ExtraLight.otf")

pygame.init()
myfont = pygame.font.Font(pygame.font.get_default_font(), 36)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
ballrect.update(1400, 500, ballrect.width, ballrect.height)

paddle_left = pygame.image.load("paddle.png")
paddle_left_rect = paddle_left.get_rect()
paddle_left_rect.update(0, 450, paddle_left_rect.width, paddle_left_rect.height)

paddle_right = pygame.image.load("paddle.png")
paddle_right_rect = paddle_right.get_rect()
paddle_right_rect.update(width-paddle_right_rect.width, 450, paddle_right_rect.width, paddle_right_rect.height)

def get_start_speed(c):
    angle = np.random.uniform(-np.pi/3, np.pi/3)
    x = np.cos(angle)*c
    y = np.sin(angle)*c
    return [x,y]


while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == 1073741905:
                print('player 1: move down')
                paddle_left_rect = paddle_left_rect.move(0,50)
                
            if event.key == 1073741906:
                print('player 1 : move up')
                paddle_left_rect = paddle_left_rect.move(0,-50)

            if event.key == 115:
                print('player 2 : move dowm')
                paddle_right_rect = paddle_right_rect.move(0,50)

            if event.key == 119:
                print('Player 2 : move up')
                paddle_right_rect = paddle_right_rect.move(0,-50)

    
    ballrect = ballrect.move(speed)
    if ballrect.left < 0:  
        print("Player 1 loses!!!")
        ballrect.update(width/2, height/2, ballrect.width, ballrect.height)
        speed = get_start_speed(2)
        player2_score = player2_score + 1
    if ballrect.right > width:
        print("Player 2 loses!!!")
        ballrect.update(width/2, height/2, ballrect.width, ballrect.height)
        speed = get_start_speed(-2)
        player1_score = player1_score + 1


    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    if ballrect.colliderect(paddle_left_rect):
        speed[0] = -speed[0]
        speed[1] = -speed[1]


    if ballrect.colliderect(paddle_right_rect):
        speed[0] = -speed[0]
        speed[1] = -speed[1]
        

    screen.fill(black)

    screen.blit(ball, ballrect)
    screen.blit(paddle_left, paddle_left_rect)
    screen.blit(paddle_right, paddle_right_rect)
    text_surface = myfont.render(f'p1: {player1_score}\np2: {player2_score}', True, green, blue)
    screen.blit(text_surface, dest=(0,0))
    

    pygame.display.flip()