from random import randint
import pygame
import sys
from copy import deepcopy

from unimon.funciones_UP.lectura import abrir_unimon
from unimon.funciones_UP.input_validation import elegir_equipo_usr, elegir_habilidades_usr, elegir_sacar_usr, elegir_movimiento_usr, cantidad_unimones, cantidad_habilidades
from unimon.pokedex.combate import restar_hp, verificar_hp, debilitado
from unimon.pokedex.estados import estado_antes, estado_danio, verificar_paralizado
from unimon.ia.npc import cambiar_npc, elegir_equipo_npc, elegir_habilidades_npc, elegir_sacar_npc, elegir_movimiento_npc
from unimon.pokedex.unimon import Unimon

unimones = abrir_unimon()

pygame.init()

# 窗口大小              / Tamaño de la ventana
ancho = 1400
altura = 800

# Menu退出选项颜色      / Color de la opción salir del menú
color_salir_menu = (255, 140, 0)
# 按钮留白距离          / Espacio de relleno de los botones
blanco_x = 20
blanco_y = 10
ancho_letras = deepcopy(ancho)
altura_letras = deepcopy(altura)

#帧率                   /  FPS
fps = pygame.time.Clock()

# 窗口标题              / Título de la ventana
screen = pygame.display.set_mode((ancho, altura))
pygame.display.set_caption("Unimon")

# 开始背景              / Fondo inicial
imagen = pygame.image.load("unimon/images/backround/inicio.jpg").convert()
backround = pygame.transform.scale(imagen, (ancho, altura))

# 字体 # Fuentes
letras_titulo = pygame.font.Font("unimon/letras/SHPinscher-Regular.otf", 180)
letras_botones = pygame.font.Font("unimon/letras/SHPinscher-Regular.otf", 65)
letras_unimones = pygame.font.Font("unimon/letras/SHPinscher-Regular.otf", 30)

# 主页标题, 生成文字图片 / Título principal, generar imagen del texto
titulo = letras_titulo.render("Unimon", True, (0, 80, 255))

# 给文字创建框         / Crear rectángulo para el texto
textRect = titulo.get_rect() 

# ================ Jugar ================

# 主页按钮             / Botón principal
jugar = letras_botones.render("Iniciar partida", True, (245, 245, 220))
jugarRect = jugar.get_rect()

# 按钮设定             / Configuración del botón
boton_inicio = pygame.Rect(0, 0, (jugarRect.width + blanco_x), (jugarRect.height + blanco_y))
boton_inicio.center = (ancho / 2, altura / 2.5)
color_boton_inicio = (0,100,255)

jugarRect.center = boton_inicio.center

# ================ Estadisticas ================
estadisticas = letras_botones.render("Estadisticas", True, (245, 245, 220))
estadisticasrRect = estadisticas.get_rect()
# 按钮设定             / Configuración del botón
boton_estadisticas = pygame.Rect(0, 0, (estadisticasrRect.width + blanco_x), (estadisticasrRect.height + blanco_y))
boton_estadisticas.center = (ancho / 2, altura / 1.8)
color_boton_estadisticas = (0,100,255)

estadisticasrRect.center = boton_estadisticas.center

# ================ Configuracion ================
configuracion = letras_botones.render("Configuracion", True, (245, 245, 220))
configuracionRect = configuracion.get_rect()
# 按钮设定             / Configuración del botón
boton_configuracion = pygame.Rect(0, 0, (configuracionRect.width + blanco_x), (configuracionRect.height + blanco_y))
boton_configuracion.center = (ancho / 2, altura / 1.4)
color_boton_configuracion = (0,100,255)

configuracionRect.center = boton_configuracion.center

# ================ Salir ================
salir = letras_botones.render("Salir", True, (0, 0, 0))
salirRect = salir.get_rect()
# 按钮设定              / Configuración del botón
boton_salir = pygame.Rect(0, 0, (salirRect.width + blanco_x), (salirRect.height + blanco_y))
boton_salir.center = (ancho / 2, altura / 1.15)
color_boton_salir = (255, 140, 0)

salirRect.center = boton_salir.center


opcion = None
color_bk_letra = []
while True:
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            #终止程序                 / Terminar el programa
            sys.exit()

        # 鼠标移到按钮上方就换颜色    / Cambiar color cuando el mouse pasa sobre el botón
        if event.type == pygame.MOUSEMOTION:
            if boton_inicio.collidepoint(mouse_pos):
                color_boton_inicio = (0, 0, 255)
            else:
                color_boton_inicio = (0,100,255)

            if boton_estadisticas.collidepoint(mouse_pos):
                color_boton_estadisticas = (0, 0, 255)
            else:
                color_boton_estadisticas = (0,100,255)

            if boton_configuracion.collidepoint(mouse_pos):
                color_boton_configuracion = (0, 0, 255)
            else:
                color_boton_configuracion = (0,100,255)

            if boton_salir.collidepoint(mouse_pos):
                color_boton_salir = (255, 0, 0)
            else:
                color_boton_salir = (255, 140, 0)

        # 按下按钮，opcion就会转换变量 / Al presionar el botón, "opcion" cambiará de valor
        if event.type == pygame.MOUSEBUTTONDOWN:
            if opcion is None:
                if event.button == 1:

                    if boton_inicio.collidepoint(event.pos):
                        opcion = "menu"

                    if boton_estadisticas.collidepoint(event.pos):
                        opcion = "estadisticas"

                    if boton_configuracion.collidepoint(event.pos):
                        opcion = "configuracion"

                    if boton_salir.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()


        if event.type == pygame.MOUSEBUTTONUP:

            if event.button == 1:

                color_boton_inicio = (0, 100, 255)
                color_boton_estadisticas = (0, 100, 255)
                color_boton_configuracion = (0, 100, 255)
                color_boton_salir = (255, 140, 0)


    # ================ Unimon ==================
    screen.blit(backround, (0, 0))
    screen.blit(titulo,textRect)

    # ================ 按钮 1 / Botón 1 ==================
    pygame.draw.rect(screen, color_boton_inicio, boton_inicio)
    screen.blit(jugar, jugarRect)
    # ================ 按钮 2 / Botón 2 ==================    
    pygame.draw.rect(screen, color_boton_estadisticas, boton_estadisticas)
    screen.blit(estadisticas, estadisticasrRect)
    # ================ 按钮 3 / Botón 3 ==================    
    pygame.draw.rect(screen, color_boton_configuracion, boton_configuracion)
    screen.blit(configuracion, configuracionRect)
    # ================ 按钮 4 / Botón 4 ==================    
    pygame.draw.rect(screen, color_boton_salir, boton_salir)
    screen.blit(salir, salirRect)

    
    # Menu页面 / Página del menú
    if opcion == "menu":
        screen.blit(backround, (0, 0))

        # unimon_por_filas是每一行应该有几个名字 / "unimon_por_filas" es cuántos nombres habrá por fila
        unimon_por_filas = 10

        # 宝可梦数量                      / Cantidad de Unimones
        cantidad = len(Unimon.todos)

        # 复制坐标                        / Copiar coordenadas
        altura_nombre = deepcopy(altura)
        ancho_nombre = deepcopy(ancho)

        # 计算每一列之间的平均距离        / Calcular la distancia promedio entre columnas
        espacio = ancho_nombre / (unimon_por_filas + 1)

        # 根据宝可梦数量计算颜色数量      / Calcular cantidad de colores según la cantidad de Unimones
        if len(color_bk_letra) < len(Unimon.todos):
            for i in range(len(Unimon.todos)):
                color_bk_letra.append((0,180,255))

        todos_unimon = []
        rects_unimon = []
        # 打印所有宝可梦的名称            / Mostrar todos los nombres de Unimon
        for i, unimon in enumerate(Unimon.todos):


            columna = i % unimon_por_filas
            fila = i // unimon_por_filas

            x = espacio * (columna + 1)
            y = 100 + fila * 100


            # 把每个宝可梦的名字变成图片，然后存储在todos_unimon / Convertir cada nombre en imagen y guardarlo en todos_unimon
            texto_unimon  = letras_unimones.render(unimon.nombre, True, (255, 255, 255), color_bk_letra[i])
            todos_unimon.append(texto_unimon )
            # 给文字创建框 / Crear rectángulo para el texto
            unimonRect = texto_unimon .get_rect()
            unimonRect.center = (x, y)

            rects_unimon.append(unimonRect)

            # 最后打印 / Dibujar finalmente
            screen.blit(todos_unimon[i],unimonRect)

        # ================ Salir menu ================
        salir_menu = letras_botones.render("Salir de menu", True, (0, 0, 0), color_salir_menu)
        salir_menuRect = salir_menu.get_rect()
        salir_menuRect.center = (ancho / 2, altura / 1.15)

        # 检测鼠标左键                                       / Detectar clic izquierdo del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:

            # 左键点击宝可梦名字，会改颜色然后等于选择了这个宝可梦 
            # Al hacer clic izquierdo en el nombre, cambiará de color y quedará seleccionado
            if event.button == 1:

                for i, rect in enumerate(rects_unimon):
                # rect = 当前宝可梦名字的矩形区域             / rect = área rectangular del nombre actual
                # event.pos = 鼠标点击的位置，例如 (300,100)  / event.pos = posición del clic del mouse, por ejemplo (300,100)
                # collidepoint() = 判断鼠标有没有点到这个区域 / collidepoint() = verificar si el mouse hizo clic en esta área
                    if rect.collidepoint(event.pos):
                        color_bk_letra[i] = (0, 0, 255)

            # 退出menu             / Salir del menú
            if salir_menuRect.collidepoint(mouse_pos):
                opcion = None


            # 右键取消选择         / Clic derecho para cancelar selección
            if event.button == 3:

                for i, rect in enumerate(rects_unimon):

                    if rect.collidepoint(event.pos):
                        color_bk_letra[i] = (0, 180, 255)
        
        # 检测鼠标移动             / Detectar movimiento del mouse
        if event.type == pygame.MOUSEMOTION:

            if salir_menuRect.collidepoint(mouse_pos):
                color_salir_menu = (255, 0, 0)
            else:
                color_salir_menu = (255, 140, 0)

        
        screen.blit(salir_menu, salir_menuRect)


        

    if opcion == "estadisticas":
        screen.blit(backround, (0, 0))


        # ================ Salir estadisticas ================
        salir_estadisticas = letras_botones.render("Salir de estadisticas", True, (0, 0, 0), color_salir_menu)
        salir_estadisticasRect = salir_estadisticas.get_rect()
        salir_estadisticasRect.center = (ancho / 2, altura / 1.15)

        # 检测鼠标左键          / Detectar clic izquierdo del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            # 退出menu          / Salir del menú
            if salir_estadisticasRect.collidepoint(mouse_pos):
                opcion = None

        # 检测鼠标移动          / Detectar movimiento del mouse
        if event.type == pygame.MOUSEMOTION:

            if salir_estadisticasRect.collidepoint(mouse_pos):
                color_salir_menu = (255, 0, 0)
            else:
                color_salir_menu = (255, 140, 0)

        screen.blit(salir_estadisticas, salir_estadisticasRect)

        
    if opcion == "configuracion":
        screen.blit(backround, (0, 0))

        Cantidad_de_unimones = letras_botones.render("Cantidad de unimones", True, (255, 255, 255), (0,100,255))
        Cantidad_de_unimonesRect = Cantidad_de_unimones.get_rect()
        Cantidad_de_unimonesRect.center = (ancho / 2, altura / 2)

        

        # ================ Salir configuracion ================
        salir_configuracion = letras_botones.render("Salir de configuracion", True, (0, 0, 0), color_salir_menu)
        salir_configuracionRect = salir_configuracion.get_rect()
        salir_configuracionRect.center = (ancho / 2, altura / 1.15)

        # 检测鼠标左键          / Detectar clic izquierdo del mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            # 退出menu          / Salir del menú
            if salir_configuracionRect.collidepoint(mouse_pos):
                opcion = None

        # 检测鼠标移动          / Detectar movimiento del mouse
        if event.type == pygame.MOUSEMOTION:

            if salir_configuracionRect.collidepoint(mouse_pos):
                color_salir_menu = (255, 0, 0)
            else:
                color_salir_menu = (255, 140, 0)

        screen.blit(salir_configuracion, salir_configuracionRect)
        screen.blit(Cantidad_de_unimones,Cantidad_de_unimonesRect)



    pygame.display.flip()

