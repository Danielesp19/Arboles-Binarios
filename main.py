import pygame
import sys
import button
import InterfazBinariTree  # Asegúrate de importar el módulo main

pygame.init()

# Dimensiones de la ventana
ventana_ancho = 400
ventana_alto = 500
screen = pygame.display.set_mode((ventana_ancho, ventana_alto))
fuente = pygame.font.Font(None, 36)
boton_arbol_binario = button.Boton(30, 150, 160, 50, "Arbol Binario")  # boton

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_arbol_binario.rect.collidepoint(evento.pos):
                ints_main=InterfazBinariTree.interfaz()
                

    screen.fill((10, 10, 10))                       

    # Botones
    boton_arbol_binario.draw(screen, (0, 128, 255), (255, 255, 255))
    pygame.display.flip()

pygame.quit()
sys.exit()