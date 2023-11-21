import pygame
import sys
import button
import JtextArea
import Jlabel
import naerytree


class interfaz:
    def __init__(self):
        self.iniciar()

    def iniciar(self):
        pygame.init()
        # Crear game window
        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 700
        padre=0
        cantidad_hijos=0
        total=0
        bandera_amplitud=False
        cont_ciclos=0
        
        

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Main Menu")

        #crear texto indicativo
        inst_jlabel1=Jlabel.JLabel(50,420,"Cantidad hijos")                  
        inst_jlabel2=Jlabel.JLabel(50,320,"Padre     ")                       
        inst_jlabel3=Jlabel.JLabel(50,520,"Nodos:   ")                       
        inst_jlabel4=Jlabel.JLabel(50,180,"Nodos totales")


        
        # Crear botones y areas de texto
        JtextArea2_padre= JtextArea.JTextArea(65,355,270,35)                  #crear textarea cantidad nodos
        JtextArea3_cantidad= JtextArea.JTextArea(65,455,270,35)              #crear textarea padre
        JtextArea1_Numeros= JtextArea.JTextArea(65,555,270,35)               #crear textarea ingreso de nodos
        JtextArea_total_nodos=JtextArea.JTextArea(65,215,270,35)

        boton_volver  = button.Boton(980, 620, 90, 50, " Salir ")          #boton
        boton_next=button.Boton(145,630,120,45," > Siguiente  ")
        boton_recorrido_amplitud=button.Boton(355,659,120,50,"siguiente")    #crear boton amplitud

        
        
        inst_arbol_nario =naerytree.NaryTree()                               #instancia arbol binario

        mostrarArbol=False                                                   #bandera para mostrar el arbol

        #bucle
        running = True
        while running:
            screen.fill((255, 255, 255))  # Rellenar la pantalla con blanco
            #titulo y decoracion
            pygame.draw.rect(screen, (20, 20, 30), (0, 0, SCREEN_WIDTH, 125))
            
            # Texto del título
            font = pygame.font.SysFont('calibri', 60, bold=True)
            texto = font.render('Arboles N-arios', True, (255, 255, 255))
            screen.blit(texto, (350, 30))

            #botones
            boton_volver.draw(screen, (230, 48, 90), (255, 255, 255))                                  
            boton_next.draw(screen, (200,200,200) , (30,30,30))
            

            
            #Dibujo de los jtextArea
            JtextArea1_Numeros.draw(screen)                         #area de ingreso numeros
            JtextArea2_padre.draw(screen)                            #area de cantidad nodos
            JtextArea3_cantidad.draw(screen)                        #area de ingreso padre
            JtextArea_total_nodos.draw(screen)

            #texto indicativo interfaz
            inst_jlabel1.draw(screen)                       #mensaje "cantidad"
            inst_jlabel2.draw(screen)                       #mensaje "padre"
            inst_jlabel3.draw(screen)                       #mensaje "nodos"
            inst_jlabel4.draw(screen)

            #ingreso y dibujo de cantidad de nodos
            if JtextArea3_cantidad.get_numeroS() and 0< JtextArea3_cantidad.get_numeroS()[-1] <=4 :            #se comprueba que el vector no este vacio y el numero menor a 19
                cantidad_hijos= JtextArea3_cantidad.get_numeroS()[-1]                                         #se asigna como cantidad al ultimo valor ingresado en el jTextArea
                inst_jlabel_cantidad=Jlabel.JLabel(210,420,str([cantidad_hijos]))                             #asignar cantidad ingresada   
                inst_jlabel_cantidad.draw(screen)                                                               #dibujar label con el numero ingresado
            else:
                inst_jlabel_cantidad=Jlabel.JLabel(210,420,"0")                                                 #informar que ningun dato ha ingresado    
                inst_jlabel_cantidad.draw(screen)                                                               #dibujar en el label numeros ingresados


            #asignar valor padre (ultimo del vector) y mostrarlo             
            if JtextArea2_padre.get_numeroS():                           #se comprueba que el vector no este vacio 
                padre=JtextArea2_padre.get_numeroS()[-1]                  #se asigna como padre al ultimo valor ingresado en el jTextArea
                inst_jlabel_padre=Jlabel.JLabel(210,320,str([padre]))     #label mostrar la padre     
                inst_jlabel_padre.draw(screen)                           #dibujar label numeros ingresados
            else:
                inst_jlabel_padre=Jlabel.JLabel(210,320,None)             #informar que ningun dato ha ingresado    
                inst_jlabel_padre.draw(screen)                           #dibujar en el label la padre


            #dibujar numeros ingresados (se debe agregar y actualizar siempre)
            inst_jlabel_numeros=Jlabel.JLabel(150,520,str(JtextArea1_Numeros.get_numeroS()))    #label mostrar la cantidad de numeros  
            inst_jlabel_numeros.draw(screen)                                                    #dibujar label numeros ingresados

            if JtextArea_total_nodos.get_numeroS()  and 0<JtextArea_total_nodos.get_numeroS()[-1]<20:
                
                total=JtextArea_total_nodos.get_numeroS()[-1]
                inst_jlabel_total_nodos=Jlabel.JLabel(210,180,str(total))
                inst_jlabel_total_nodos.draw(screen)
            else:
                inst_jlabel_total_nodos=Jlabel.JLabel(210,180,"0")
                inst_jlabel_total_nodos.draw(screen)

            boton_recorrido_amplitud.draw(screen,(190,190,190) , (30,30,30))
            
            if bandera_amplitud:
                jlabel_recorrido_ampli= Jlabel.JLabel(500,560,inst_arbol_nario.mostrar_amplitud())
                jlabel_recorrido_ampli.draw(screen)


            if mostrarArbol:
                inst_arbol_nario.initiate_drawing(screen, SCREEN_WIDTH // 1.5, 150, 90)  # mostrar inorden
            
            for event in pygame.event.get():
                #salir
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_volver.rect.collidepoint(event.pos):           #detectar colision con evento de raton
                        #animacion boton
                        boton_volver.draw(screen, (255, 8, 20), (0, 0, 0))
                        pygame.display.flip()

                    if boton_recorrido_amplitud.rect.collidepoint(event.pos):
                        mostrarArbol=not mostrarArbol 

                    if boton_next.rect.collidepoint(event.pos):
                        
                        if total>0:
                            if total>cont_ciclos:
                                if len((JtextArea1_Numeros.get_numeroS()))>=cantidad_hijos:
                                    if cont_ciclos==0:
                                        inst_arbol_nario.insert_node(None,int(padre)) 
                                        cont_ciclos+=1
                                        for i in range(cantidad_hijos):                                                               # ingresar solo la cantidad asignada
                                            inst_arbol_nario.insert_node(padre,int(JtextArea1_Numeros.get_numeroS()[i]))                    #Bandera dibuja el arbol
                                            cont_ciclos+=1


                                    else:
                                        for i in range(len(JtextArea1_Numeros.get_numeroS()) - cantidad_hijos, len(JtextArea1_Numeros.get_numeroS())):
                                            inst_arbol_nario.insert_node(padre, int(JtextArea1_Numeros.get_numeroS()[i]))
                                            cont_ciclos += 1
                                    print('exito')
                    if boton_volver.rect.collidepoint(event.pos):
                        self.iniciar()
                #enviar eventos jtext area
                JtextArea2_padre.handle_event(event)
                JtextArea3_cantidad.handle_event(event)
                JtextArea1_Numeros.handle_event(event)
                JtextArea_total_nodos.handle_event(event)
            
            pygame.display.flip()
            
        pygame.quit()
        sys.exit()