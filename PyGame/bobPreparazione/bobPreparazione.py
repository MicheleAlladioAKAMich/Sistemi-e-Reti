'''
Author: Michele Alladio
es: 
Il nostro amico Bob dopo alcune commissioni in giro per la città di Flatland deve rientrare a casa. 
Purtroppo Bob soffre di momentanee perdite di memoria!
Questa volta la sua amnesia dura ben 60 minuti e durante questi 60 minuti Bob adotta la seguente strategia 
per tentare di rientrare a casa. Ogni minuto decide a caso tra:
procedere 10 m verso Nord
procedere 10 m verso Sud
procedere 10 m verso Est
procedere 10 m verso Ovest
Simulare l’intero percorso compiuto da Bob, supponendo che il punto di partenza abbia coordinate (0,0) 
e salvarlo all’interno di un dizionario opportunamente strutturato.
Disegnare il percorso compiuto da Bob dentro una schermata di pygame.
Infine salvare il percorso di Bob dentro un file .csv opportunamente strutturato.
'''
import sys, pygame, random, csv #librerie

NERO = (0,0,0)    #RGB
BIANCO = (255,255,255)
GIALLO = (255,255,0)
VERDE = (0,255,0)

dimensione = 10
BASE = 600
ALTEZZA = 600

def drawgrid(): #disegno la griglia
    for x in range(0, BASE, dimensione):    #disegna una piastrella ogni 100 per l'intera LARGHEZZA
        for y in range(0, ALTEZZA, dimensione): #disegna una piastrella ogni 100 per l'intera ALTEZZA
            piastrella = pygame.Rect(x, y, dimensione, dimensione) 
            pygame.draw.rect(screen, BIANCO, piastrella, 1)

def BobPartenza():  #partenza di Bob (quadrato verde)
    partenza = pygame.Rect(BASE/2, ALTEZZA/2, dimensione, dimensione)   #centrato nella griglia
    pygame.draw.rect(screen, VERDE, partenza)

def bobAggiornamento(x, y): #ogni volta disegna un quadrato giallo sulla griglia in base alle coordinate generate
    aggiornamento = pygame.Rect(BASE/2 + x, ALTEZZA/2 + y, dimensione, dimensione) 
    pygame.draw.rect(screen, GIALLO, aggiornamento)

def main():
    global screen   #schermo

    pygame.init()
    screen = pygame.display.set_mode((BASE, ALTEZZA))    #richiede una tupla
    screen.fill(NERO)   #colore schermo

    dizCoordinate = {} #partenza

    #coordinate di partenza che verranno aggiornate 
    currentX = 0
    currentY = 0

    for minuti in range(1,61):  #parte dal primo passo fino ad arrivare alla fine dell'ora
        posizioneAttuale = []   #lista delle posizioni [x,y]

        sceltaRandom = random.randint(1,4)  #scelta random della direzione

        if sceltaRandom == 1:   #nord
            currentY -= 10

        elif sceltaRandom == 2: #sud
            currentY += 10
            
        elif sceltaRandom == 3: #est
            currentX -= 10
            
        elif sceltaRandom == 4: #ovest
            currentX += 10
            
        #aggiornamento della lista
        posizioneAttuale.append(currentX)
        posizioneAttuale.append(currentY)

        #creo il dizionario ---> minuto attuale : [x,y]
        dizCoordinate[minuti] = posizioneAttuale

        #bobAggiornamento(currentX, currentY)

    print(dizCoordinate)    #stampo il dizionario

    with open('coordinateBob.csv', 'w', newline='') as fileBob:  #scrittura nel file
        writer = csv.writer(fileBob)
        for minuto, coordinata in dizCoordinate.items():
            writer.writerow([minuto, coordinata[0], coordinata[1]])

    while True:
        drawgrid()  #disegno la griglia
        BobPartenza()   #disegno la partenza di Bob

        for _, coordinata in dizCoordinate.items():
            bobAggiornamento(coordinata[0], coordinata[1])  #aggiorno la posizione di Bob sulla griglia

        #gestione eventi nella finestra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #se l'evento è l'uscita
                pygame.quit()
                sys.exit()  #il programma termina in maniera pulita

        pygame.display.update()

if __name__ == "__main__":
    main()