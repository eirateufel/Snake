import pygame
import os
from random import *
from queue import Queue
from collections import deque

from Score import Score
from snake import Snake


def draw_point():
    global radius, formsize, squareSize, x_point_pos, y_point_pos
    pygame.draw.circle(screen, point_color, (x_point_pos, y_point_pos), radius)

def move_point():
    global formsize, squareSize, x_point_pos, y_point_pos
    x_point_pos = (randint(squareSize, formSize - squareSize)//squareSize)*squareSize
    y_point_pos = (randint(squareSize, formSize - squareSize)//squareSize)*squareSize


#form
formSize = 600
pygame.init()
screen = pygame.display.set_mode((formSize, formSize))

#square
squareSize = 20

#point
radius = 3
x_point_pos = (randint(squareSize/2, formSize - squareSize/2)//squareSize)*squareSize
y_point_pos = (randint(squareSize/2, formSize - squareSize/2)//squareSize)*squareSize
point_color = (255, 165, 0)

#Score
pygame.font.init()
#font = pygame.font.SysFont('Comic Sans MS', 30)
font = pygame.font.Font(os.path.join("res", "fonts", 'manaspc.ttf'), 16)
score = Score(screen, font)

#Snake
snake = Snake(screen, 20)

time = 2
x_speed_direction = 1
y_speed_direction = 0

pygame.init()
screen = pygame.display.set_mode((formSize, formSize))

clock = pygame.time.Clock()

done = False
counter = 1
eaten = False
button = False

while not done:

    screen.fill((0, 0, 0))
    button = False
    eaten = False

    if x_point_pos == (snake.x_pos + squareSize/2) and y_point_pos == (snake.y_pos + squareSize/2):
        snake.eat_point()
        
        counter += 1
        if counter % 10 == 0:
            time = time * 1.2
        move_point()
        eaten = True
        score.increase()
        
    if not eaten:
        draw_point()

    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not button:
                if snake.get_speed_x() == 0:
                    snake.set_speed(1, 0)
                    button = True
                    continue
                else:
                    continue
            if event.key == pygame.K_LEFT and not button:
                if snake.get_speed_x() == 0:
                    snake.set_speed(-1, 0)
                    button = True
                    continue
                else:
                    continue
            if event.key == pygame.K_UP and not button:
                if snake.get_speed_y() == 0:
                    snake.set_speed(0, -1)
                    button = True
                    continue
                else:
                    continue
            if event.key == pygame.K_DOWN and not button:
                if snake.get_speed_y() == 0:
                    snake.set_speed(0, 1)
                    button = True
                    continue
                else:
                    continue

    snake.move()
    snake.draw()

    score.draw()

    intersect_result = snake.is_self_intersect()
    if intersect_result != 0:
        score.decrease(intersect_result)
        if score.get_value() < 0:
            snake.set_speed(0, 0)
            screen.fill((0, 0, 0))
            pygame.font.Font(None, 80)
            text = font.render("GAME OVER!", False, (255, 255, 255))
            screen_width = screen.get_rect()[2]
            screen_height = screen.get_rect()[3]
            screen.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2))



    pygame.display.flip()
    clock.tick(time)
    
