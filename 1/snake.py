import pygame
from random import *
from queue import Queue
from collections import deque
from Score import Score

def draw_body(x_body, y_body):
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x_body, y_body, squareSize, squareSize))

def move():
    global x_pos, y_pos

    x_pos += x_speed_direction * squareSize
    y_pos += y_speed_direction * squareSize
    x_body.append(x_pos)
    y_body.append(y_pos)
    x_body.popleft()
    y_body.popleft()
    
def move_eaten():
    global x_pos, y_pos

    x_pos += x_speed_direction * squareSize
    y_pos += y_speed_direction * squareSize
    x_body.append(x_pos)
    y_body.append(y_pos)

def set_speed(x, y):
    global x_speed_direction, y_speed_direction
    x_speed_direction = x
    y_speed_direction = y

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
x_pos = screen.get_rect()[2] / 2 - squareSize / 2 
y_pos = screen.get_rect()[3] / 2 - squareSize / 2

x_body = deque()
x_body.append(x_pos)
y_body = deque()
y_body.append(y_pos)


#point
radius = 3
x_point_pos = (randint(squareSize/2, formSize - squareSize/2)//squareSize)*squareSize
y_point_pos = (randint(squareSize/2, formSize - squareSize/2)//squareSize)*squareSize
point_color = (255, 165, 0)

time = 30/20
x_speed_direction = 1
y_speed_direction = 0

pygame.init()
screen = pygame.display.set_mode((formSize, formSize))

#Score
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
score = Score(screen, font)

clock = pygame.time.Clock()

done = False
counter = 1
eaten = False
button = False

while not done:
    
    screen.fill((0, 0, 0))
    button = False
    eaten = False
        
    for i in range (0, counter):
        draw_body(x_body[i], y_body[i])

    if x_point_pos == (x_pos + squareSize/2) and y_point_pos == (y_pos + squareSize/2):            
        x_body.appendleft(x_body[0])
        y_body.appendleft(y_body[0])
        
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
                if x_speed_direction == 0:
                    set_speed(1, 0)
                    button = True
                    continue
                else:
                    continue
            if event.key == pygame.K_LEFT and not button:
                if x_speed_direction == 0:
                    set_speed(-1, 0)
                    button = True
                    continue
                else:
                    continue
            if event.key == pygame.K_UP and not button:
                if y_speed_direction == 0:
                    set_speed(0, -1)
                    button = True
                    continue
                else:
                    continue
            if event.key == pygame.K_DOWN and not button:
                if y_speed_direction == 0:
                    set_speed(0, 1)
                    button = True
                    continue
                else:
                    continue
    move()
    score.draw()
    pygame.display.flip()
    clock.tick(time)
    
