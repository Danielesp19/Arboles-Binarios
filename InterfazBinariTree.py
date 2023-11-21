import pygame
import sys
import button
import JtextArea
import Jlabel
import binarytree


class interfaz:
    def __init__(self):
        pygame.init()
        # Crear game window
        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 700
        raiz=0
        cantidad_numeros=0
        bandera_recorridos=False
        bandera_preorden=False
        bandera_inorden=False
        bandera_posorden=False
        bandera_amplitud=False
        mostrarArbol=False                                                   #bandera para mostrar el arbol

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Main Menu")

        #crear texto indicativo
        inst_jlabel1=Jlabel.JLabel(50,320,"Cantidad nodos")                  #crear label cantidad
        inst_jlabel2=Jlabel.JLabel(50,420,"Raiz     ")                       #crear label raiz
        inst_jlabel3=Jlabel.JLabel(50,520,"Nodos:   ")                       #crear label nodos

        # Crear botones y areas de texto
        JtextArea2_Raiz= JtextArea.JTextArea(65,455,270,35)                  #crear textarea cantidad nodos
        JtextArea3_cantidad= JtextArea.JTextArea(65,355,270,35)              #crear textarea raiz
        JtextArea1_Numeros= JtextArea.JTextArea(65,555,270,35)               #crear textarea ingreso de nodos

        boton_volver  = button.Boton(980, 620, 90, 50, " Salir ")          #boton
        boton_recorridos = button.Boton(55, 150,265,50," Recorridos  ")      #boton
        boton_triangulo = button.Boton(320, 150,30,50," V ")                  #boton
        boton_crear_arbol=button.Boton(150,630,100,45," > Crear  ")

        boton_recorrido_inorden=button.Boton(55,200,120,49,"In-orden")
        boton_recorrido_preorden=button.Boton(185,200,120,49,"pre-orden")
        boton_recorrido_posorden=button.Boton(55,249,120,50,"pos-orden")
        boton_recorrido_amplitud=button.Boton(185,249,120,50,"amplitud")

        
        
        inst_arbol_bynario =binarytree.BinaryTree()                          #instancia arbol binario
        
        #bucle
        running = True
        while running:
            screen.fill((255, 255, 255))  # Rellenar la pantalla con blanco
            
            #titulo y decoracion
            pygame.draw.rect(screen, (20, 20, 30), (0, 0, SCREEN_WIDTH, 125))
            # Texto del título
            font = pygame.font.SysFont('calibri', 60, bold=True)
            texto = font.render('Arboles binarios', True, (255, 255, 255))
            screen.blit(texto, (350, 30))
            #botones
            boton_volver.draw(screen, (230, 48, 90), (255, 255, 255))                    
            boton_recorridos.draw(screen, (230, 60, 90), (255, 255, 255))                
            boton_crear_arbol.draw(screen, (200,200,200) , (30,30,30))
            boton_triangulo.draw(screen,(200,200,200) , (30,30,30))
            
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
                inst_jlabel_cantidad=Jlabel.JLabel(210,320,str([cantidad_numeros]))                             #asignar cantidad ingresada   
                inst_jlabel_cantidad.draw(screen)                                                               #dibujar label con el numero ingresado
            else:
                inst_jlabel_cantidad=Jlabel.JLabel(210,320,"0")                                                 #informar que ningun dato ha ingresado    
                inst_jlabel_cantidad.draw(screen)                                                               #dibujar en el label numeros ingresados

            #asignar valor raiz (ultimo del vector) y mostrarlo             
            if JtextArea2_Raiz.get_numeroS():                           #se comprueba que el vector no este vacio 
                raiz=JtextArea2_Raiz.get_numeroS()[-1]                  #se asigna como raiz al ultimo valor ingresado en el jTextArea
                inst_jlabel_raiz=Jlabel.JLabel(210,420,str([raiz]))     #label mostrar la raiz     
                inst_jlabel_raiz.draw(screen)                           #dibujar label numeros ingresados
            else:
                inst_jlabel_raiz=Jlabel.JLabel(210,420,"None")          #informar que ningun dato ha ingresado    
                inst_jlabel_raiz.draw(screen)                           #dibujar en el label la raiz

            #dibujar numeros ingresados (se debe agregar y actualizar siempre)
            inst_jlabel_numeros=Jlabel.JLabel(150,520,str(JtextArea1_Numeros.get_numeroS()))    #label mostrar la cantidad de numeros  
            inst_jlabel_numeros.draw(screen)                                                    #dibujar label numeros ingresados

            #
            if bandera_recorridos:
                pygame.draw.rect(screen, (200, 200, 200), (55, 200, 295, 100))
                
                
                boton_recorrido_inorden.draw(screen,(190,190,190) , (30,30,30))
                boton_recorrido_preorden.draw(screen,(190,190,190) , (30,30,30))
                boton_recorrido_posorden.draw(screen,(190,190,190) , (30,30,30))
                boton_recorrido_amplitud.draw(screen,(190,190,190) , (30,30,30))

            if bandera_preorden:
                jlabel_recorrido_pre= Jlabel.JLabel(500,550,inst_arbol_bynario.mostrar_preorden())
                jlabel_recorrido_pre.draw(screen)
            if bandera_inorden:
                jlabel_recorrido_in= Jlabel.JLabel(500,520,inst_arbol_bynario.mostrar())
                jlabel_recorrido_in.draw(screen)
            if bandera_posorden:
                jlabel_recorrido_pos= Jlabel.JLabel(500,580,inst_arbol_bynario.mostrar_posorden())
                jlabel_recorrido_pos.draw(screen)
            if bandera_amplitud:
                jlabel_recorrido_ampli= Jlabel.JLabel(500,610,inst_arbol_bynario.mostrar_amplitud())
                jlabel_recorrido_ampli.draw(screen)

            #se muestraa el arbol
            if mostrarArbol:
                inst_arbol_bynario.iniciardibujo(screen, SCREEN_WIDTH // 1.5, 150, 90)  # mostrar inorden

            for event in pygame.event.get():
                #salir
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_volver.rect.collidepoint(event.pos):           #detectar colision con evento de raton
                        #animacion boton
                        boton_volver.draw(screen, (255, 8, 20), (0, 0, 0))
                        pygame.display.flip()

                    if boton_recorridos.rect.collidepoint(event.pos):       #detectar colision con evento de raton
                        #animacion boton
                        boton_recorridos.draw(screen, (255, 8, 20), (0, 0, 0))
                        pygame.display.flip() 

                        #mostrar recorridos
                        bandera_recorridos= not bandera_recorridos
                    
                    if boton_recorrido_preorden.rect.collidepoint(event.pos):
                        bandera_preorden= not bandera_preorden
                    if boton_recorrido_inorden.rect.collidepoint(event.pos):
                        bandera_inorden= not bandera_inorden
                    if boton_recorrido_posorden.rect.collidepoint(event.pos):
                        bandera_posorden= not bandera_posorden
                    if boton_recorrido_amplitud.rect.collidepoint(event.pos):
                        bandera_amplitud= not bandera_amplitud
                    
                    if boton_crear_arbol.rect.collidepoint(event.pos):
                        
                        if len((JtextArea1_Numeros.get_numeroS()))>=cantidad_numeros and cantidad_numeros>0 and raiz!=0 :
                            inst_arbol_bynario.insertion_node(raiz)
                            for i in range(cantidad_numeros):                                                               # ingresar solo la cantidad asignada
                                inst_arbol_bynario.insertion_node(int(JtextArea1_Numeros.get_numeroS()[i]))
                            mostrarArbol=not mostrarArbol                                                                  #Bandera dibuja el arbol


                #enviar eventos jtext area
                JtextArea2_Raiz.handle_event(event)
                JtextArea3_cantidad.handle_event(event)
                JtextArea1_Numeros.handle_event(event)

            pygame.display.flip()

        pygame.quit()
        sys.exit()