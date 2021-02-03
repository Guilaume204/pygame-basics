import sys
import numpy as np
import pygame
from time import sleep
pygame.init()

size = width, height = 1600, 900
speed = [2, 2]
black = 60, 60, 60
BLACK=(0,0,0)

screen = pygame.display.set_mode(size)

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
    angle = np.random.random()*np.pi
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
                print('move up')
                paddle_left_rect = paddle_left_rect.move(0,10)
                
            if event.key == 1073741906:
                print('move down')
                paddle_left_rect = paddle_left_rect.move(0,-10)
                
        

    ballrect = ballrect.move(speed)
    if ballrect.left < 0:  
        print("Player 1 loses!!!")
        ballrect.update(width/2, height/2, ballrect.width, ballrect.height)
        speed = get_start_speed(5)
    if ballrect.right > width:
        print("Player 2 loses!!!")
        ballrect.update(width/2, height/2, ballrect.width, ballrect.height)
        speed = get_start_speed(5)


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
    

    pygame.display.flip()