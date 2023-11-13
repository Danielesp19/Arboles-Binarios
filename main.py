import pygame
import sys
import button
import JtextArea
import Jlabel
import binarytree


pygame.init()

# Crear game window
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
raiz=0
cantidad_numeros=0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#crear texto indicativo
inst_jlabel1=Jlabel.JLabel(50,150,"Cantidad nodos")     #crear label cantidad
inst_jlabel2=Jlabel.JLabel(50,250,"Raiz     ")          #crear label raiz
inst_jlabel3=Jlabel.JLabel(50,350,"Nodos:   ")          #crear label nodos



# Crear botones y areas de texto
JtextArea1_Numeros= JtextArea.JTextArea(65,385,270,35)          #crear textarea ingreso de nodos
JtextArea2_Raiz= JtextArea.JTextArea(65,285,270,35)          #crear textarea cantidad nodos
JtextArea3_cantidad= JtextArea.JTextArea(65,185,270,35)          #crear textarea raiz


boton_arbol_binario = button.Boton(30, 500, 160, 50, "Arbol Binario")
boton_arbol_nario= button.Boton(220, 500,160,50,"Arbol Eneario")




vector_nodos = []


    #inst_arbol_binario.draw_binary_tree(screen,raiz, SCREEN_WIDTH // 1.5, 50, 150)
    
    



#bucle
running = True
while running:
    for event in pygame.event.get():
        #salir
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boton_arbol_binario.rect.collidepoint(event.pos):    #detectar colision con evento de raton
                if cantidad_numeros > 0:
                    llenar()
                    
            
            if boton_arbol_nario.rect.collidepoint(event.pos):      #detectar colision con evento de raton
                print("¡Haz clic en el botón!")
        
        #enviar eventos jtext area
        
        JtextArea2_Raiz.handle_event(event)
        JtextArea3_cantidad.handle_event(event)
        JtextArea1_Numeros.handle_event(event)

    screen.fill((255, 255, 255))  # Rellenar la pantalla con blanco
    
    #titulo y decoracion
    pygame.draw.rect(screen, (0,0,0), (0, 0, SCREEN_WIDTH, 125))
    pygame.draw.rect(screen, (128, 128, 128), ((SCREEN_WIDTH/2)-115, 125, SCREEN_WIDTH,SCREEN_HEIGHT ))
    font = pygame.font.Font(None, 36)
    texto = font.render('Arboles', True, (255, 255, 255))
    screen.blit(texto, (480,65))


    #botones
    boton_arbol_binario.draw(screen, (0, 128, 255), (255, 255, 255))              # Dibujar el botón en la pantalla
    boton_arbol_nario.draw(screen, (0, 128, 255), (255, 255, 255))                # Dibujar el botón en la pantalla


    #Dibujo de los jtextArea
    JtextArea1_Numeros.draw(screen)                         #area de ingreso numeros
    JtextArea2_Raiz.draw(screen)                            #area de cantidad nodos
    JtextArea3_cantidad.draw(screen)                        #area de ingreso raiz

    #texto indicativo interfaz
    inst_jlabel1.draw(screen)                       #mensaje "cantidad"
    inst_jlabel2.draw(screen)                       #mensaje "raiz"
    inst_jlabel3.draw(screen)                       #mensaje "nodos"



    #ingreso y dibujo de cantidad de nodos
    if JtextArea3_cantidad.get_numeroS() and 0< JtextArea3_cantidad.get_numeroS()[-1] <=19 :            #se comprueba que el vector no este vacio y el numero menor a 19
        cantidad_numeros= JtextArea3_cantidad.get_numeroS()[-1]                                         #se asigna como cantidad al ultimo valor ingresado en el jTextArea
        inst_jlabel_cantidad=Jlabel.JLabel(210,150,str([cantidad_numeros]))                             #asignar cantidad ingresada   
        inst_jlabel_cantidad.draw(screen)                                                               #dibujar label con el numero ingresado
    else:
        inst_jlabel_cantidad=Jlabel.JLabel(210,150,"0")                                                 #informar que ningun dato ha ingresado    
        inst_jlabel_cantidad.draw(screen)                                                               #dibujar en el label numeros ingresados


    #asignar valor raiz (ultimo del vector) y mostrarlo             
    if JtextArea2_Raiz.get_numeroS():                           #se comprueba que el vector no este vacio 
        raiz=JtextArea2_Raiz.get_numeroS()[-1]                  #se asigna como raiz al ultimo valor ingresado en el jTextArea
        inst_jlabel_raiz=Jlabel.JLabel(210,250,str([raiz]))     #label mostrar la raiz     
        
        inst_jlabel_raiz.draw(screen)                           #dibujar label numeros ingresados
    else:
        inst_jlabel_raiz=Jlabel.JLabel(210,250,"None")          #informar que ningun dato ha ingresado    
        inst_jlabel_raiz.draw(screen)                           #dibujar en el label la raiz


    #dibujar numeros ingresados (se debe agregar y actualizar siempre)
    inst_jlabel_numeros=Jlabel.JLabel(150,350,str(JtextArea1_Numeros.get_numeroS()))    #label mostrar la cantidad de numeros  
    inst_jlabel_numeros.draw(screen)                                                    #dibujar label numeros ingresados

    def llenar():
        inst_arbol_bynario=binarytree.BinaryTree()                                              #instancia arbol binario
        inst_arbol_bynario.insertion_node(raiz)                                                 #insertar raiz
        for i in range (cantidad_numeros):                                                      #ingresar solo la cantidad asignada
            inst_arbol_bynario.insertion_node(JtextArea1_Numeros.get_numeroS()[i])              #ingresar los numeros como nodos
        
        inst_arbol_bynario.mostrar()                                                            #mostrar inorden
        
        
    
        
        

    pygame.display.flip()

pygame.quit()
sys.exit()






