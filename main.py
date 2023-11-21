import webbrowser
import pygame
import sys
import button
import InterfazBinariTree
import InterfazNAriTree
import Jlabel


pygame.init()
# Dimensiones de la ventana
ventana_ancho = 650
ventana_alto = 413
screen = pygame.display.set_mode((ventana_ancho, ventana_alto))

imagen = pygame.image.load("C:/Users/Usuario/Downloads/arboles (1) (1).jpg")
imagen_rect = imagen.get_rect()
imagen_rect.center = (ventana_ancho // 2, ventana_alto // 2)

imagen2 = pygame.image.load("C:/Users/Usuario/Downloads/screenshot_a0658c0e-5a2c-4d37-b4b2-837e32d2072f__1___1_-removebg-preview.png")
imagen_rect2 = imagen2.get_rect()
imagen_rect2.width = 150  # Ajustar el ancho de la segunda imagen
imagen_rect2.topleft = (230, 0)  # Ajustar la posición de la segunda imagen

fuente = pygame.font.Font(None, 36)
boton_arbol_binario = button.Boton(30, 120, 160, 50, "Arbol Binario")  # boton
boton_arbol_nario= button.Boton(30, 200, 160, 50, "Arbol N-ario")

nombre = "Daniel Espitia"
color_nombre = (250, 250, 250)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_arbol_binario.rect.collidepoint(evento.pos):
                ints_main = InterfazBinariTree.interfaz()
            if boton_arbol_nario.rect.collidepoint(evento.pos):
                ins_Naritree=InterfazNAriTree.interfaz()
            if 260 <= evento.pos[0] <= 620 and 40 <= evento.pos[1] <= 393:
                # Abre la URL cuando se hace clic en la segunda imagen
                webbrowser.open("https://github.com/Danielesp19/Arboles-Binarios")  # Reemplaza con tu URL
    screen.fill((10, 10, 10))
    screen.blit(imagen, imagen_rect)
    screen.blit(imagen2, imagen_rect2)
    # Botones
    boton_arbol_binario.draw(screen, (250, 250, 250), (0, 0, 0))
    boton_arbol_nario.draw(screen, (250, 250, 250), (0, 0, 0))
    texto_renderizado = fuente.render(nombre, True, color_nombre)
    screen.blit(texto_renderizado, (345, 365))
    pygame.display.flip()

pygame.quit()
sys.exit()