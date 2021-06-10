'''
Authors: Michele Alladio, Samuele Forneris

Tramite un microbit controlla Kirbi ed evita i laser rossi!
'''

import pygame, random, serial, sys, time, threading, queue
import tkinter as tk

root = tk.Tk()  #viene utilizzato per calcolare le dimensioni dello schermo (funziona sia su Windows che su Linux)

WIDTH = int(root.winfo_screenwidth())    #calcolo dell'altezza dello schermo
HEIGHT = int(root.winfo_screenheight())    #calcolo dell'altezza dello schermo
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

laserDimentions = 10

dt = 1
gamma = 0.05
q = queue.Queue()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

avatar = pygame.image.load("H:\\sist_reti\\4AROB\\Python\\Microbit\\Kirbi.png")
avatar = pygame.transform.scale(avatar,(int(WIDTH/25), int(HEIGHT/15)))
gameOver = pygame.image.load("H:\\sist_reti\\4AROB\\Python\\Microbit\\gameOver.png")
gameOver = pygame.transform.scale(gameOver, (WIDTH, HEIGHT))


class Read_Microbit(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        #serial config
        port = "COM3"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            time.sleep(0.01)

rm = Read_Microbit() #legge i dati da microbit

def collisionControl(avatarPosition, X_List, Y_List, score, scoreNumber):
    for xLaser in X_List:   #ciclo le x dei laser
        if avatarPosition.centerx + WIDTH/50 >= xLaser and avatarPosition.centerx - WIDTH/50 <= xLaser: #se l'immagine si sovrappone ad un laser
            #immagine di game over
            screen.blit(gameOver,(0,0))
            screen.blit(score,(10,20))
            screen.blit(scoreNumber,(WIDTH/9,20))
            pygame.display.update()
            time.sleep(3)
            #chiusura controllata del thread
            rm.terminate()
            rm.join()
            #chiusura controllata di pygame
            pygame.quit()
            sys.exit()

    for yLaser in Y_List: #ciclo le y dei laser
        if avatarPosition.centery + HEIGHT/30 > yLaser and avatarPosition.centery - HEIGHT/30 <= yLaser: #se l'immagine si sovrappone ad un laser
            #immagine di game over
            screen.blit(gameOver,(0,0))
            screen.blit(score,(10,20))
            screen.blit(scoreNumber,(WIDTH/9,20))
            pygame.display.update()
            time.sleep(3)
            #chiusura controllata del thread
            rm.terminate()
            rm.join()
            #chiusura controllata di pygame
            pygame.quit()
            sys.exit()   

def noticeLaser(laserNumber, X_List, Y_List):
    for element in range(laserNumber):  #crea un numero di laser random
        direction = random.randint(0,1) #direzione laser(verticale/orizzontale)
        posX = random.randint(0,WIDTH)  #X laser random
        posY = random.randint(0,HEIGHT) #Y laser random

        if direction == 0:  #laser random orizzontale
            laser = pygame.Rect(0, posY, WIDTH, laserDimentions) 
            pygame.draw.rect(screen, WHITE, laser)
            #aggiornamento liste coordinate
            X_List.append(0)
            Y_List.append(posY)
        else:   #laser random verticale
            laser = pygame.Rect(posX, 0, laserDimentions, HEIGHT) 
            pygame.draw.rect(screen, WHITE, laser)
            #aggiornamento liste coordinate
            X_List.append(posX)
            Y_List.append(0)
        
    return X_List, Y_List

def noticeLaser2(laserNumber, X_List, Y_List):
    for element in range(laserNumber):
        if X_List[element] == 0:    #laser orizzontale
            laser = pygame.Rect(0, Y_List[element], WIDTH, laserDimentions) 
            pygame.draw.rect(screen, WHITE, laser)
        else:   #laser verticale
            laser = pygame.Rect(X_List[element], 0, laserDimentions, HEIGHT) 
            pygame.draw.rect(screen, WHITE, laser)
            

def drawLaser(laserNumber, X_List, Y_List):
     for element in range(laserNumber):
        if X_List[element] == 0:    #laser orizzontale
            laser = pygame.Rect(0, Y_List[element], WIDTH, laserDimentions) 
            pygame.draw.rect(screen, RED, laser)
        else:   #laser verticale
            laser = pygame.Rect(X_List[element], 0, laserDimentions, HEIGHT) 
            pygame.draw.rect(screen, RED, laser)

def windowBorderControl(speed, avatarRect):
    if avatarRect.left <= 0:    #uscita da sinistra
        speed[0] = 1
    elif avatarRect.right >= WIDTH: #uscita da destra
        speed[0] = -1

    if avatarRect.top <= 0: #uscita dall'alto
        speed[1] = 1
    elif avatarRect.bottom >= HEIGHT:   #uscita dal basso
        speed[1] = -1
    
        
def main():
    avatarRect = avatar.get_rect()  #identifica il bordo dell'immagine
    #centro dell'immagine
    avatarRect.centerx = WIDTH//2
    avatarRect.centery = HEIGHT//2

    pygame.init()
    myFont = pygame.font.SysFont("Comic Sans MS", 30)
    score = myFont.render('SCORE:', False, WHITE)
    levelNumber = 1 #numero del livello per un corretto controllo del tempo

    running = True  #il programma esegue
    rm.start()  #start del thread
    speed = [0, 0]  #velocità orizzontale e verticale

    #posizione dell'avatar all'inizio del gioco (centrato rispetto alla finestra)
    avatarX = WIDTH/2
    avatarY = HEIGHT/2 

    while True: #10 livelli
        scoreNumber = myFont.render(str(int((levelNumber-1)/2)), False, WHITE)
        #liste delle coordinate
        X_List = []
        Y_List = []

        laserNumber = random.randint(20,30) #numero di laser random
        spawned = False   
        delay = 0   #tempo trascorso (azzeramento dopo ogni livello)

        while delay < 2*levelNumber:    #per 4 secondi
            acc = q.get()
            #calcolo delle velocità
            speed[0] = (1.-gamma)*speed[0] + dt*acc[0]/1024.
            speed[1] = (1.-gamma)*speed[1] + dt*acc[1]/1024.

            q.task_done()
            avatarRect = avatarRect.move(speed) #moviemento dell'immagine

            delay = time.perf_counter() #tempo trascorso

            screen.fill(BLACK)  #azzeramento della situazione precedente
            screen.blit(avatar, avatarRect)

            if not spawned: #primo spawn dei laser nei quatro secondi
                X_List, Y_List = noticeLaser(laserNumber, X_List, Y_List)    #avviso spawn dei laser
            else:   #se nei quattro secondi è già avvenuto lo spawn dei laser
                noticeLaser2(laserNumber, X_List, Y_List)   #si ripete lo spawn nelle stesse posizioni 
            spawned = True #controllo per verificare l'avvenuto spawn dei laser

            windowBorderControl(speed, avatarRect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #se l'evento è l'uscita
                    pygame.quit()
                    sys.exit()  #il programma termina in maniera pulita
                    
            pygame.display.update()

        spawned = False
        levelNumber+=1
        
        while delay < 2*levelNumber:    #per 4 secondi
            acc = q.get()
            speed[0] = (1.-gamma)*speed[0] + dt*acc[0]/1024.
            speed[1] = (1.-gamma)*speed[1] + dt*acc[1]/1024.
            q.task_done()
            avatarRect = avatarRect.move(speed)

            delay = time.perf_counter() #tempo trascorso 

            screen.fill(BLACK)  #azzeramento della situazione precedente
            screen.blit(avatar, avatarRect)

            drawLaser(laserNumber, X_List, Y_List)    #spawn dei laser
            
            screen.blit(avatar, avatarRect)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:   #se l'evento è l'uscita
                    pygame.quit()
                    sys.exit()  #il programma termina in maniera pulita
                    
            collisionControl(avatarRect, X_List, Y_List, score, scoreNumber)
            windowBorderControl(speed, avatarRect)

            pygame.display.update()
        
        levelNumber += 1    #incremento del numero del livello
    
    rm.terminate()
    rm.join()
        

if __name__ == "__main__":
    main()
