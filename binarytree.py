import pygame
import sys
from pygame.locals import *

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insertion_node(self, value):
        new = Node(value)
        if self.root is None:
            self.root = new
        else:
            self.recursive_insert(self.root, value)

    def recursive_insert(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.recursive_insert(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self.recursive_insert(current.right, value)

    def draw_binary_tree(self, screen, node, x, y, horizontal_spacing):
        if node is not None:
            self.draw_node(screen, node, x, y)
            if node.left is not None:
                x_left = x - horizontal_spacing
                y_left = y + 60
                self.draw_binary_tree(screen, node.left, x_left, y_left, horizontal_spacing // 2)
                pygame.draw.line(screen, (0, 0, 0), (x, y + 20), (x_left, y_left - 20), 2)
            if node.right is not None:
                x_right = x + horizontal_spacing
                y_right = y + 60
                self.draw_binary_tree(screen, node.right, x_right, y_right, horizontal_spacing // 2)
                pygame.draw.line(screen, (0, 0, 0), (x, y + 20), (x_right, y_right - 20), 2)

    def iniciardibujo(self, screen, x, y, horizontal_spacing):
        current = self.root
        self.draw_binary_tree(screen, current, x, y, horizontal_spacing)

    def draw_node(self, screen, node, x, y):
        pygame.draw.circle(screen, (255, 188, 28), (x, y), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(str(node.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

    def mostrar(self):
        if self.root is not None:
            self._mostrar_recursivamente(self.root)

    def _mostrar_recursivamente(self, node):
        if node is not None:
            self._mostrar_recursivamente(node.left)
            print(node.value)
            self._mostrar_recursivamente(node.right)

