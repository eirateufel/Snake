import pygame
from collections import deque

class Snake:
    def __init__(self, screen, square_size):
        self.screen = screen
        self.screen_width = self.screen.get_rect()[2]
        self.screen_height = self.screen.get_rect()[3]

        self.x_pos = screen.get_rect()[2] / 2 - square_size / 2
        self.y_pos = screen.get_rect()[3] / 2 - square_size / 2
        self.square_size = square_size

        self.x_body = deque()
        self.x_body.append(self.x_pos)
        self.y_body = deque()
        self.y_body.append(self.y_pos)

        self.x_speed_direction = 0
        self.y_speed_direction = 1

        self.counter = 1

    def move(self):
        self.x_pos += self.x_speed_direction * self.square_size
        if self.x_pos > self.screen_width:
            self.x_pos = self.x_pos - self.screen_width
        elif self.x_pos < 0:
            self.x_pos = self.screen_width - self.x_pos

        self.y_pos += self.y_speed_direction * self.square_size
        if self.y_pos > self.screen_height:
            self.y_pos = self.y_pos - self.screen_height
        elif self.y_pos < 0:
            self.y_pos = self.screen_height - self.y_pos

        self.x_body.append(self.x_pos)
        self.y_body.append(self.y_pos)
        self.x_body.popleft()
        self.y_body.popleft()

    def set_speed(self, x, y):
        self.x_speed_direction = x
        self.y_speed_direction = y

    def get_speed_x(self):
        return self.x_speed_direction

    def get_speed_y(self):
        return self.y_speed_direction

    def is_self_intersect(self):
        for i in range(0, self.counter - 1):  # off with her head
            if self.x_body[i] == self.x_pos and self.y_body[i] == self.y_pos:
                negativeScores = 0
                for j in range(0, i + 1):
                    self.x_body.popleft()
                    self.y_body.popleft()
                    self.counter -= 1
                    negativeScores -= 15
                return negativeScores
        return 0

    def eat_point(self):
        self.x_body.appendleft(self.x_body[0])
        self.y_body.appendleft(self.y_body[0])
        self.counter += 1

    def draw(self):
        for i in range(0, self.counter):
            pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.x_body[i], self.y_body[i], self.square_size, self.square_size))

