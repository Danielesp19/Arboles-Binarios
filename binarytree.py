import pygame
import sys

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

    def draw_binary_tree(self, window, root, x, y, horizontal_spacing):
        if root is not None:
            self.draw_node(window, root, x, y)
            if root.left is not None:
                x_left = x - horizontal_spacing
                y_left = y + 160
                self.draw_binary_tree(window, root.left, x_left, y_left, horizontal_spacing // 3)
                pygame.draw.line(window, (0, 0, 0), (x, y + 30), (x_left, y_left - 30), 2)
            if root.right is not None:
                x_right = x + horizontal_spacing
                y_right = y + 160
                self.draw_binary_tree(window, root.right, x_right, y_right, horizontal_spacing // 3)
                pygame.draw.line(window, (0, 0, 0), (x, y + 30), (x_right, y_right - 30), 2)

    def draw_node(self, window, node, x, y):
        pygame.draw.circle(window, (255, 188, 28), (x, y), 20)
        font = pygame.font.Font(None, 36)
        text = font.render(str(node.value), True, (255, 255, 255))
        text_rect = text.get_rect(center=(x, y))
        window.blit(text, text_rect)

    def mostrar(self):
        if self.root is not None:
            self._mostrar_recursivamente(self.root)

    def _mostrar_recursivamente(self, nodo):
        if nodo is not None:
            self._mostrar_recursivamente(nodo.left)
            print(nodo.value)
            self._mostrar_recursivamente(nodo.right)