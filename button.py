import pygame
import sys

import pygame

#button class
class Boton:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, surface, color, text_color):
        pygame.draw.rect(surface, color, self.rect)
        font = pygame.font.Font(None, 30)
        text = font.render(self.text, True, text_color)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
	
