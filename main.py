import pygame
import sys
import button
import JtextArea
import Jlabel

pygame.init()

# Crear game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")


inst_jlabel1=Jlabel.JLabel(50,150,"Cantidad nodos")     #crear label cantidad
inst_jlabel2=Jlabel.JLabel(50,250,"Raiz     ")          #crear label raiz
inst_jlabel3=Jlabel.JLabel(50,350,"Nodos:   ")          #crear label nodos



# Crear un botón y areas de texto
JtextArea1_Numeros= JtextArea.JTextArea(65,385,270,35)          #crear textarea ingreso de nodos
JtextArea2_Raiz= JtextArea.JTextArea(65,285,270,35)          #crear textarea cantidad nodos
JtextArea3_cantidad= JtextArea.JTextArea(65,185,270,35)          #crear textarea raiz


boton_arbol_binario = button.Boton(30, 500, 160, 50, "Arbol Binario")
boton_arbol_nario= button.Boton(220, 500,160,50,"Arbol Eneario")





running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_arbol_binario.rect.collidepoint(event.pos):
                print("¡Haz clic en el botón!")
            if boton_arbol_nario.rect.collidepoint(event.pos):
                print("¡Haz clic en el botón!")
        JtextArea1_Numeros.handle_event(event)
        JtextArea2_Raiz.handle_event(event)
        JtextArea3_cantidad.handle_event(event)

    screen.fill((255, 255, 255))  # Rellenar la pantalla con blanco
    
    #titulo y decoracion
    pygame.draw.rect(screen, (0,0,0), (0, 0, SCREEN_WIDTH, 125))
    font = pygame.font.Font(None, 36)
    texto = font.render('Arboles', True, (255, 255, 255))
    screen.blit(texto, (490,65))

    boton_arbol_binario.draw(screen, (0, 128, 255), (255, 255, 255))              # Dibujar el botón en la pantalla
    boton_arbol_nario.draw(screen, (0, 128, 255), (255, 255, 255))             # Dibujar el botón en la pantalla


    JtextArea1_Numeros.draw(screen)                         #area de ingreso numeros
    JtextArea2_Raiz.draw(screen)                            #area de cantidad nodos
    JtextArea3_cantidad.draw(screen)                        #area de ingreso raiz


    inst_jlabel1.draw(screen)                       #mensaje "cantidad"
    inst_jlabel2.draw(screen)                       #mensaje "raiz"
    inst_jlabel3.draw(screen)                       #mensaje "nodos"


    #dibujar cantidad de nodos
    cantidad_numeros=0
    if JtextArea3_cantidad.get_numeroS() and JtextArea3_cantidad.get_numeroS()[-1] <=19 :       #se comprueba que el vector tenga 
        cantidad_numeros= JtextArea3_cantidad.get_numeroS()[-1]
        inst_jlabel_cantidad=Jlabel.JLabel(210,150,str([cantidad_numeros]))                             #label mostrar los numeros ingresados    
        inst_jlabel_cantidad.draw(screen)                                                               #dibujar label numeros ingresados
    else:
        inst_jlabel_cantidad=Jlabel.JLabel(210,150,"0")                                                 #label mostrar los numeros ingresados    
        inst_jlabel_cantidad.draw(screen)                                                               #dibujar label numeros ingresados


    #asignar valor raiz (ultimo del vector) y mostrarlo             
    raiz=0
    if JtextArea2_Raiz.get_numeroS():
        raiz=JtextArea2_Raiz.get_numeroS()[-1]
        inst_jlabel_raiz=Jlabel.JLabel(210,250,str([raiz]))    #label mostrar la raiz     
        inst_jlabel_raiz.draw(screen)                        #dibujar label numeros ingresados
    else:
        inst_jlabel_raiz=Jlabel.JLabel(210,250,"None")       #label mostrar la raiz     
        inst_jlabel_raiz.draw(screen) 

    #dibujar numeros ingresados se deben crear y actualizar siempre
    inst_jlabel_numeros=Jlabel.JLabel(150,350,str(JtextArea1_Numeros.get_numeroS()))    #label mostrar la cantidad de numeros  
    inst_jlabel_numeros.draw(screen)                                                    #dibujar label numeros ingresados


    pygame.display.flip()

pygame.quit()
sys.exit()






