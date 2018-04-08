import pygame


class Score:
    def __init__(self, screen, font):
        self.text = "Score"
        self.value = 0
        self.font = font
        self.screen = screen
        self.screen_width = self.screen.get_rect()[2]
        self.scree_height = self.screen.get_rect()[3]

    def draw(self):
        text = self.font.render(self.text + ":" + str(self.value), False, (255, 255, 255))
        self.screen.blit(text, (self.screen_width - text.get_width() - 10, 0))

    def increase(self):
        self.value += 10
