import pygame
import sys
font_size=20
text_color=(0, 0, 0)
bg_color=(255, 255, 255)
border_color=(0, 0, 0)
border_width=5
class JTextArea:
    def __init__(self, x, y, width, height ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.font_size = font_size
        self.text_color = text_color
        self.bg_color = bg_color
        self.border_color = border_color
        self.border_width = border_width
        self.is_editing = False
        self.text_entradas = []

    def draw(self, surface):
        # Dibuja el rectángulo de fondo
        pygame.draw.rect(surface, self.bg_color, self.rect)

        # Dibuja el borde alrededor del rectángulo de fondo
        border_rect = pygame.Rect(self.rect.x - self.border_width, self.rect.y - self.border_width,self.rect.width + 2 * self.border_width, self.rect.height + 2 * self.border_width)
        pygame.draw.rect(surface, self.border_color, border_rect, self.border_width)

        # Dibuja el texto en el centro del rectángulo
        font = pygame.font.Font(None, self.font_size)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.is_editing = True
            else:
                self.is_editing = False
        elif event.type == pygame.KEYDOWN and self.is_editing:
            if event.key == pygame.K_RETURN:
                try:
                    # Intenta convertir el texto a un número
                    num = int(self.text)
                    if num >0:
                        self.text_entradas.append(num)
                except ValueError:
                    # Ignora la entrada si no es un número
                    pass
                finally:
                    self.text = ""

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def get_numeroS(self):
        return self.text_entradas
    
    def vaciar_vector(self):
        self.text_entradas = []
# Inicialización de Pygame
