import pygame
import sys
from pygame.locals import *

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class NaryTree:
    def __init__(self):
        self.root = None

    def insert_node(self, parent_value, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            parent_node = self.find_node(self.root, parent_value)
            if parent_node:
                parent_node.children.append(new_node)

    def find_node(self, current, value):
        if current.value == value:
            return current
        for child in current.children:
            node = self.find_node(child, value)
            if node:
                return node
        return None

    def draw_tree(self, screen, node, x, y, horizontal_spacing):
        if node is not None:
            self.draw_node(screen, node, x, y)
            if node.children:
                num_children = len(node.children)
                x_offset = -(num_children - 1) * horizontal_spacing / 2
                for child in node.children:
                    x_child = x + x_offset
                    y_child = y + 60
                    self.draw_tree(screen, child, x_child, y_child, horizontal_spacing // 2)
                    pygame.draw.line(screen, (0, 0, 0), (x, y + 20), (x_child, y_child - 20), 2)
                    x_offset += horizontal_spacing

    def initiate_drawing(self, screen, x, y, horizontal_spacing):
        current = self.root
        self.draw_tree(screen, current, x, y, horizontal_spacing)

    def draw_node(self, screen, node, x, y):
        pygame.draw.circle(screen, (255, 188, 28), (x, y), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(str(node.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)