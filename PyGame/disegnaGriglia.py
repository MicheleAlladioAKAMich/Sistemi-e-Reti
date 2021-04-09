"""
Author: Michele Alladio
es: disegnare una griglia con un ostacolo mediante l'uso della libreria pygame
"""

import pygame
import sys  #uscita da python mediante la chiusura della finestra
DIMENSIONI = (600,600)  #tupla
NERO = (0,0,0)    #RGB
BIANCO = (255,255,255)
ROSSO = (255,0,0)

def drawgrid():
    dimensione = 50  #piastrella
    for x in range(0, DIMENSIONI[0], dimensione):    #disegna una piastrella ogni 50 per l'intera LARGHEZZA
        for y in range(0, DIMENSIONI[1], dimensione):
            piastrella = pygame.Rect(x, y, dimensione, dimensione) 
            pygame.draw.rect(screen, BIANCO, piastrella, 1)

    ostacolo = pygame.Rect(50, 100, dimensione, dimensione)
    pygame.draw.rect(screen, ROSSO, ostacolo)

def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(DIMENSIONI)    #richiede una tupla
    screen.fill(NERO)

    while True:
        drawgrid()  #disegna la griglia
   
        #gestione eventi nella finestra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #se l'evento è l'uscita
                pygame.quit()
                sys.exit()  #il programma termina in maniera pulita
        
        pygame.display.update()


if __name__ == "__main__":
    main()