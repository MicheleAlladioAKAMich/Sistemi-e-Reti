"""
Author: Michele Alladio
es: robot che si muove in una stanza evitando gli ostacoli usando l'algoritmo di Daistra
"""
import sys, pygame, random

NERO = (0,0,0)    #RGB
BIANCO = (255,255,255)
ROSSO = (255,0,0)
VERDE = (0,255,0)

pavimento =     [[ 0, 0, 0,-1,-1],   #0 -> libero, -1 -> ostacolo
                 [-1, 0, 0, 0,-1],
                 [ 0, 0,-1,-1,-1],
                 [ 0, 0,-1, 0, 0],
                 [-1, 0, 0, 0, 0],
                 [-1,-1,-1, 0, 0]]

dimensione = 100    #dimensione di una piastrella
ALTEZZA = len(pavimento) * dimensione   #altezza griglia
BASE = len(pavimento[0]) * dimensione   #base griglia

def drawgrid():
    for x in range(0, BASE, dimensione):    #disegna una piastrella ogni 100 per l'intera LARGHEZZA
        for y in range(0, ALTEZZA, dimensione): #disegna una piastrella ogni 100 per l'intera ALTEZZA
            piastrella = pygame.Rect(x, y, dimensione, dimensione) 
            pygame.draw.rect(screen, BIANCO, piastrella, 1)

def drawObstacles():
    myfont = pygame.font.SysFont("Comic Sans MS", 30)   #font della scritta
    cntNumeri = 1   

    for contY in range(0, len(pavimento)):
        for contX in range(0, len(pavimento[0])):

            label = myfont.render(str(cntNumeri), 1, BIANCO)  #impostazioni della scritta

            if pavimento[contY][contX] == -1:    
                #spostamento nella cella corretta ottenuto tramite la moltiplicazione dei contatori con la dimensione   
                contX *= dimensione
                contY *= dimensione  

                #disegno dell'ostacolo    
                ostacolo = pygame.Rect(contX, contY, dimensione, dimensione)
                pygame.draw.rect(screen, ROSSO, ostacolo)
                
                #reset dei valori dei contatori
                contX = int(contX / dimensione)
                contY = int(contY / dimensione)

            else:
                contX *= dimensione
                contY *= dimensione  

                screen.blit(label, (contX + (dimensione/3), contY + (dimensione/3)))

                contX = int(contX / dimensione)
                contY = int(contY / dimensione)

                cntNumeri += 1

def drawRobot(posX, posY):
        robot = pygame.Rect(posX, posY, dimensione, dimensione) 
        pygame.draw.rect(screen, VERDE, robot)

'''def pavimentoRandom(pavimentoVuoto):
    for celleVerticali in range(6):
        for celleOrizzontali in range(5):
            cellaRandom = random.randint(0, 1)
            pavimentoVuoto[celleVerticali][celleOrizzontali] = cellaRandom
    
    return pavimentoVuoto'''


def main():
    global screen   #schermo
    
    pygame.init()
    screen = pygame.display.set_mode((BASE, ALTEZZA))    #richiede una tupla
    screen.fill(NERO)   #colore schermo

    dizCoord = {}

    contCelleLibere = 0

    startX = 0
    startY = 0

    prossimaX = 0
    prossimaY = 0

    for contY in range(0, len(pavimento)):
        for contX in range(0, len(pavimento[0])):

            if pavimento[contY][contX] == 0:             
                pavimento[contY][contX] = contCelleLibere   #assegamento del numero alla cella corrispondente
                contCelleLibere += 1

    print(f"Numero di celle libere: {contCelleLibere}")

    for contY in range(0, len(pavimento)):
        for contX in range(0, len(pavimento[0])):

            spazLiberi = [] #lista degli spazi liberi (si resetta ad ogni ciclo for)

            if pavimento[contY][contX] != -1:

                if contY != 0:      #controllo sinsitra
                    if pavimento[contY - 1][contX] != -1:
                        spazLiberi.append(pavimento[contY - 1][contX])
                    
                if contX != 0:  #controllo alto
                    if pavimento[contY][contX - 1] != -1:
                        spazLiberi.append(pavimento[contY][contX - 1])

                if contX != (len(pavimento[contY]) - 1):    #controllo basso
                    if pavimento[contY][contX + 1] != -1:
                        spazLiberi.append(pavimento[contY][contX + 1])


                if contY != (len(pavimento) - 1):       #controllo destra
                    if pavimento[contY + 1][contX] != -1:
                        spazLiberi.append(pavimento[contY + 1][contX])

                dizCoord[pavimento[contY][contX]] = spazLiberi  #creo dizionario numero cella : lista celle a contatto

    print(dizCoord)

    while True:
        drawgrid()  #disegna la griglia
        drawObstacles()    #disegna gli ostacoli sulla griglia
        drawRobot(startX, startY)
   
        #gestione eventi nella finestra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #se l'evento è l'uscita
                pygame.quit()
                sys.exit()  #il programma termina in maniera pulita
            
            elif event.type == pygame.KEYDOWN:   #se viene premuto un qualsiasi tasto
                if event.key == pygame.K_UP:
                    startY -= dimensione

                if event.key == pygame.K_DOWN:
                    startY += dimensione

                if event.key == pygame.K_RIGHT:
                    for k in dizCoord[pavimento[prossimaY][prossimaX]]:
                        if k == prossimaX+1:
                            startX += dimensione
                   
                    prossimaX += 1

                if event.key == pygame.K_LEFT:
                    startX -= dimensione

        pygame.display.update()

if __name__ == "__main__":
    main()