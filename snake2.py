import curses
import random
import time
# from playsound import playsound
from curses import textpad
import threading
#menu
menu= ["nuevo juego" "salir"]
hi_score = 0

# prueba en git
alto=25
ancho=50
pantalla = curses.initscr()

puntuación = 0
score_text = "Puntuación: {}", format (puntuación)
hi_score_text = "Puntuación alta: {}", format (hi_score)
#stdscr.addtr(1, sw//2-len(score_text))//2,score_text)
#stdscr.agregar (1,4,hi_score_text)
#=================
#Color de pantalla
#==================
curses.start_color() 
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_YELLOW)

#============================
#===inicializacion de curses=====
#============================

curses.noecho()
curses.cbreak()
curses.curs_set(0)
pantalla.keypad(True)
pantalla.nodelay(True)


#score =+10
    
#============================
#===inicializacion de snake=====
#===y de la fruta=====
#============================
x=0
y=0
snake=[[y,x]]
fruta=[random.randrange(alto),random.randrange(ancho)]
pantalla.addstr(fruta[0],fruta[1],"#")
mov_horizontal = 1
mov_vertical = 0
#otra fruta
fruta=[random.randrange(alto),random.randrange(ancho)]
pantalla.addstr(fruta[0],fruta[1],"ñ")
mov_horizontal= 1
mov_vertical = 0
# pantalla

#def pantalla (stdscr):
#    curses.curs_set(0)
#    stdscr.nodelay(1)
#    stdscr.timeout(100)
##    current_row = 0
 #   print (menu(stdscr,current_row))
#============================
#===comienzo del juego=====
#============================
while True:    
    #leemos la tecla
    tecla = pantalla.getch()        
    #le asignamos una dirección a cada cursor
    if tecla==curses.KEY_LEFT:
        mov_horizontal = -1
        mov_vertical = 0
    elif tecla==curses.KEY_RIGHT:
        mov_horizontal = 1
        mov_vertical = 0
    elif tecla==curses.KEY_UP:
        mov_horizontal = 0
        mov_vertical = -1
    elif tecla==curses.KEY_DOWN:
        mov_horizontal = 0
        mov_vertical = 1
    elif tecla== 10
        
    x = (x + mov_horizontal) % ancho
    y = (y + mov_vertical) % alto

    posicion=[y,x]

    #si nos comemos una parte de snake, el juego se enoja y se sale    
    if posicion in snake:
        break

    snake.insert(0,posicion)    
    #ponemos una pausa, probá que sucede si la comentás
    time.sleep(0.1)

    #verificamos si nos morfamos una fruta
    if fruta in snake:        
        fruta=[random.randrange(alto),random.randrange(ancho)]
        pantalla.addstr(fruta[0],fruta[1],"#")
    elif fruta in snake:
        fruta=[random.randrange(alto),random.randrange(ancho)]
        pantalla.addstr(fruta[0], fruta[1],"ñ")
    #sino, borramos la colita
    else:
        ultimaposicion = snake.pop()
        pantalla.addstr(ultimaposicion[0],ultimaposicion[1]," ")


    #else:  
    #    ultimaposicion = snake.pop()
    #    pantalla.addstr(ultimaposicion[0],ultimaposicion[1]," ")
    #dibujamos la cabeza
        pantalla.addstr(snake[0][0],snake[0][1],"#")
    #   pantalla.addstr(snake[0][0], snake[0][1],"ñ")

    #pantalla.addstr(y,x, "#")   
#Ponemos todo en su lugar    
curses.nocbreak()
pantalla.keypad(False)
curses.echo()
curses.endwin()
