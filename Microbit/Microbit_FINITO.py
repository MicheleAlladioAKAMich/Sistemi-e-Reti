import pygame, random, serial, sys, time, threading, queue

WIDTH = 1200
HEIGHT = 800
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
avatar = pygame.transform.scale(avatar,(int(WIDTH/20), int(HEIGHT/15)))

avatarRect = avatar.get_rect()
avatarRect.centerx = WIDTH//2
avatarRect.centery = HEIGHT//2

X_List = []
Y_List = []

class Read_Microbit(threading.Thread):
    def init(self):
        threading.Thread.init(self)
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        #serial config
        port = "/dev/tty0"
        s = serial.Serial(port)
        s.baudrate = 115200
        while self._running:
            data = s.readline().decode() 
            acc = [float(x) for x in data[1:-3].split(",")]
            q.put(acc)
            time.sleep(0.01)

def controlloCollisioni(avatarPosition):
    for xLaser in X_List:
        if avatarPosition.left >= xLaser or avatarPosition.left <= xLaser+laserDimentions:
            print("hai perso")
            pygame.quit()
            sys.exit()

    for yLaser in Y_List:
        if avatarPosition.top >= yLaser or avatarPosition.bottom <= yLaser+laserDimentions:
            print("hai perso")
            pygame.quit()
            sys.exit()
    

def noticeLaser(laserNumber):

    for element in range(laserNumber):
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
    
        
def main():
    running = True
    rm = Read_Microbit() #legge i dati da microbit
    rm.start()
    pygame.init()
    speed = [0, 0]

    levelNumber = 1 #numero del livello per un corretto controllo del tempo
    avatarX = WIDTH/2
    avatarY = HEIGHT/2 

    for situation in range(10): #10 livelli

        X_List = []
        Y_List = []

        laserNumber = random.randint(10,30) #numero di laser random
        spawned = False    
        delay = 0   #tempo trascorso (azzeramento dopo ogni livello)

        while delay < 4*levelNumber:    #per 4 secondi
            acc = q.get()
            speed[0] = (1.-gamma)*speed[0] + dt*acc[0]/1024.
            speed[1] = (1.-gamma)*speed[1] + dt*acc[1]/1024.
            q.task_done()
            avatarRect = avatarRect.move(speed)

            delay = time.perf_counter() #tempo trascorso

            screen.fill(BLACK)  #azzeramento della situazione precedente
            screen.blit(avatar, avatarRect)

            if not spawned:
                X_List, Y_List = noticeLaser(laserNumber)    #avviso spawn dei laser
            else:
                noticeLaser2(laserNumber, X_List, Y_List)
            spawned = True #controllo per verificare l'avvenuto spawn dei laser

            for event in pygame.event.get():
                if event.type == pygame.QUIT:   #se l'evento è l'uscita
                    pygame.quit()
                    sys.exit()  #il programma termina in maniera pulita

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        avatarY-=5
                    elif event.key == pygame.K_DOWN:
                        avatarY+=5
                    elif event.key == pygame.K_LEFT:
                        avatarX-=5
                    elif event.key == pygame.K_RIGHT:
                        avatarX+=5
            
            pygame.display.update()

        spawned = False
        levelNumber+=1
        
        while delay < 4*levelNumber:    #per 4 secondi
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
        
            controlloCollisioni(avatarRect)

            pygame.display.update()
        
        levelNumber += 1    #incremento del numero del livello
    
    rm.terminate()
    rm.join()

if __name__ == "__main__":
    main()
