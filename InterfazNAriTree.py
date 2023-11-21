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

        SCREEN_WIDTH = 1100
        SCREEN_HEIGHT = 700
        padre = 0
        cantidad_hijos = 0
        total = 0
        bandera_amplitud = False
        cont_ciclos = 0
        

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Main Menu")

        inst_jlabel1 = Jlabel.JLabel(50, 420, "Cantidad hijos")
        inst_jlabel2 = Jlabel.JLabel(50, 320, "Padre     ")
        inst_jlabel3 = Jlabel.JLabel(50, 520, "Nodos:   ")
        inst_jlabel4 = Jlabel.JLabel(50, 180, "Nodos totales")

        JtextArea2_padre = JtextArea.JTextArea(65, 355, 270, 35)
        JtextArea3_cantidad = JtextArea.JTextArea(65, 455, 270, 35)
        JtextArea1_Numeros = JtextArea.JTextArea(65, 555, 270, 35)
        JtextArea_total_nodos = JtextArea.JTextArea(65, 215, 270, 35)

        boton_volver = button.Boton(980, 620, 90, 50, " Salir ")
        boton_next = button.Boton(145, 630, 120, 45, " > Siguiente  ")
        boton_crear = button.Boton(SCREEN_WIDTH // 1.6, 150, 120, 50, "crear")
        boton_recorrido= button.Boton(480,630,80,30,"recorrido")

        inst_arbol_nario = naerytree.NaryTree()

        mostrarArbol = False

        running = True
        while running:
            screen.fill((255, 255, 255))
            pygame.draw.rect(screen, (20, 20, 30), (0, 0, SCREEN_WIDTH, 125))

            font = pygame.font.SysFont('calibri', 60, bold=True)
            texto = font.render('Arboles N-arios', True, (255, 255, 255))
            screen.blit(texto, (350, 30))

            boton_volver.draw(screen, (230, 48, 90), (255, 255, 255))
            boton_next.draw(screen, (200, 200, 200), (30, 30, 30))
            boton_crear.draw(screen, (190, 190, 190), (30, 30, 30))
            boton_recorrido.draw(screen,(200, 200, 200), (30, 30, 30))

            JtextArea1_Numeros.draw(screen)
            JtextArea2_padre.draw(screen)
            JtextArea3_cantidad.draw(screen)
            JtextArea_total_nodos.draw(screen)

            inst_jlabel1.draw(screen)
            inst_jlabel2.draw(screen)
            inst_jlabel3.draw(screen)
            inst_jlabel4.draw(screen)

            if JtextArea_total_nodos.get_numeroS() and 0 < JtextArea_total_nodos.get_numeroS()[-1] < 20:
                if cont_ciclos==0:
                    total = JtextArea_total_nodos.get_numeroS()[-1]
                    inst_jlabel_total_nodos = Jlabel.JLabel(210, 180, str(total))
                    inst_jlabel_total_nodos.draw(screen)
                else:
                    inst_jlabel_total_nodos = Jlabel.JLabel(210, 180, str(total))
                    inst_jlabel_total_nodos.draw(screen)
            else:
                inst_jlabel_total_nodos = Jlabel.JLabel(210, 180, "0")
                inst_jlabel_total_nodos.draw(screen)

            if JtextArea3_cantidad.get_numeroS() and 0 < JtextArea3_cantidad.get_numeroS()[-1] <= total-1:
                cantidad_hijos = JtextArea3_cantidad.get_numeroS()[-1]
                inst_jlabel_cantidad_hijos = Jlabel.JLabel(210, 420, str([cantidad_hijos]))
                inst_jlabel_cantidad_hijos.draw(screen)
            else:
                inst_jlabel_cantidad_hijos = Jlabel.JLabel(210, 420, "0")
                inst_jlabel_cantidad_hijos.draw(screen)

            if JtextArea2_padre.get_numeroS():
                padre = JtextArea2_padre.get_numeroS()[-1]
                inst_jlabel_padre = Jlabel.JLabel(210, 320, str([padre]))
                inst_jlabel_padre.draw(screen)
            else:
                inst_jlabel_padre = Jlabel.JLabel(210, 320, None)
                inst_jlabel_padre.draw(screen)

            inst_jlabel_numeros = Jlabel.JLabel(150, 520, str(JtextArea1_Numeros.get_numeroS()))
            inst_jlabel_numeros.draw(screen)

            if bandera_amplitud:
                jlabel_recorrido_ampli = Jlabel.JLabel(565, 665, inst_arbol_nario.mostrar_amplitud())
                jlabel_recorrido_ampli.draw(screen)

            print(JtextArea1_Numeros.get_numeroS())
            if mostrarArbol:
                inst_arbol_nario.initiate_drawing(screen, SCREEN_WIDTH // 1.5, 300, 90)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if boton_volver.rect.collidepoint(event.pos):
                        boton_volver.draw(screen, (255, 8, 20), (0, 0, 0))
                        pygame.display.flip()

                    if boton_crear.rect.collidepoint(event.pos):
                        mostrarArbol = not mostrarArbol

                    if boton_next.rect.collidepoint(event.pos):
                        if total > 0 and total >= cantidad_hijos:
                            if len((JtextArea1_Numeros.get_numeroS())) >= cantidad_hijos:
                                if cont_ciclos == 0:
                                    inst_arbol_nario.insert_node(None, int(padre))
                                    for i in range(cantidad_hijos):
                                        inst_arbol_nario.insert_node(padre, int(JtextArea1_Numeros.get_numeroS()[i]))
                                    cont_ciclos += 1
                                    total=total-1
                                else:
                                    for i in range(cantidad_hijos):
                                        inst_arbol_nario.insert_node(padre, int(JtextArea1_Numeros.get_numeroS()[i]))
                                        cont_ciclos += 1
                                total=total-cantidad_hijos
                                
                                JtextArea1_Numeros.vaciar_vector()
                                JtextArea2_padre.vaciar_vector()
                                JtextArea3_cantidad.vaciar_vector()

                                print('exito')
                    if boton_volver.rect.collidepoint(event.pos):
                        del self
                    if boton_recorrido.rect.collidepoint(event.pos):
                        bandera_amplitud=not bandera_amplitud

                JtextArea2_padre.handle_event(event)
                JtextArea3_cantidad.handle_event(event)
                JtextArea1_Numeros.handle_event(event)
                JtextArea_total_nodos.handle_event(event)

            pygame.display.flip()

        pygame.quit()
        sys.exit()