'''
Author: Michele Alladio
es:
Ipotesi:
considerate stringhe lunghe al massimo 12 caratteri
i caratteri ammessi sono le cifre da “0” a “9”, il carattere spazio (“ “) e le lettere minuscole 
dell’alfabeto italiano da “a” a “z”
ognuno di questi caratteri può essere codificato su 5 bit.

Create un programma in Python3 che:

crei un dizionario che abbia come chiave ciascuno dei caratteri di cui sopra e come valori le liste di bit 
(numeri interi 0 oppure 1) corrispondenti alla codifica binaria su 5 bit. La codifica può essere inventata da voi
es: {“b” : [1,0,1,0,1],.............}

chieda all’utente una stringa composta secondo le ipotesi di cui sopra.

converta la stringa inserita dall’utente in una lista di liste effettuando la conversione da ogni 
carattere alla corrispondente lista di bit

disegni il qr code, ovvero rappresenti la lista di lista su uno screen di Pygame, usando celle nere per i bit a 1 e 
celle bianche per i bit a 0

salvi la lista di liste di cui al punto 3 all’interno di un file .csv.


BONUS:
l’utente può decidere se inserire una stringa oppure il nome di un file csv: nel secondo caso il programma apre 
il file .csv e rappresenta il qr code su uno screen di Pygame.

'''

import sys, pygame, csv #librerie

NERO = (0,0,0)    #RGB
BIANCO = (255,255,255)

dimensione = 50
ALTEZZA = 600
BASE = 250

def disegnaQrCode(lista):   
    for verticale in range(len(lista)): #la finestra è alta come la stringa
        for orizzontale in range(5):    #la finestra è larga come il numero di bit di una lettera
            pezzoQR = pygame.Rect(orizzontale * dimensione, verticale * dimensione, dimensione, dimensione) #creo un pezzo del QR, traslandolo della sua posizione nella lista * 50 
            if(lista[verticale][orizzontale] == 0): #se il bit è 0 il pezzo del QR sarà bianco 
                pygame.draw.rect(screen, BIANCO, pezzoQR)

def creaLista(stringa, dizionarioCaratteri):
    lista = []

    for lettera in stringa: #ciclo le lettere nella stringa
        for elementi in dizionarioCaratteri.items():    #ciclo il dizionario
            if lettera == elementi[0]:  #appena trovo la lettera carico nella lista la sua codifica
                lista.append(elementi[1])
    
    return lista    #restituisco la lista

def letturaStringa():
    scelta = input("Scrivere file per leggere la stringa dal file oppure tastiera per inserire la stringa manualmente: ")

    if scelta == 'file': 
        nomeFile = input("Inserisci il nome del file: ")    #chiedo il nome del file
        fileStringa = open(nomeFile, "r")   #apro il file in lettura (percorso assoluto)
        
        for riga in fileStringa:    #leggo la riga del file e la salvo nella stringa
            stringa = riga
        fileStringa.close() #chiudo il file

    elif scelta == 'tastiera':  
        stringa = input("Inserisci una stringa (massimo 12 caratteri): ")   #inserisco la stringa da tastiera
    else:
        return -1   #se la scelta non esiste returno -1 (caso di errore)

    return stringa  #returno la stringa

def stampaListaFile(lista):
    fileOutput = input("Inserisci il nome del file in cui salvare la lista: ")
    with open(fileOutput, 'w', newline='') as fileSalvaStato:  #scrittura nel file
        writer = csv.writer(fileSalvaStato)
        for element in lista:  #ciclo gli elementi 
            writer.writerow(element)    #li scrivo nel file'''

def finestraPygame(lista):
    while True:

        disegnaQrCode(lista)    #disegno il QR

        #gestione eventi nella finestra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #se l'evento è l'uscita
                pygame.quit()
                sys.exit()  #il programma termina in maniera pulita

        pygame.display.update() #update della finestra

def main():

    global screen   #schermo
    screen = pygame.display.set_mode((BASE, ALTEZZA))    #settaggio dello schermo (richiede una tupla)
    screen.fill(NERO)   #colore schermo
    pygame.init()   #inizializzazione di pygame

    dizionarioCaratteri = {'a':[0,0,0,0,0], 'b':[0,0,0,0,1], 'c':[0,0,0,1,0], 'd':[0,0,0,1,1], 'e':[0,0,1,0,0], 'f':[0,0,1,0,1], 
                            'g':[0,0,1,1,0], 'h':[0,0,1,1,1],'i':[0,1,0,0,0], 'l':[0,1,0,0,1],'m':[0,1,0,1,0], 'n':[0,1,0,1,1],
                            'o':[0,1,1,0,0], 'p':[0,1,1,0,1],'q':[0,1,1,1,0], 'r':[0,1,1,1,1],'s':[1,0,0,0,0], 't':[1,0,0,0,1],
                            'u':[1,0,0,1,0], 'v':[1,0,0,1,1],'z':[1,0,1,0,0], '0':[1,0,1,0,1],'1':[1,0,1,1,0], '2':[1,0,1,1,1],
                            '3':[1,1,0,0,0], '4':[1,1,0,0,1], '5':[1,1,0,1,0], '6':[1,1,0,1,1],'7':[1,1,1,0,0], '8':[1,1,1,0,1], 
                            '9':[1,1,1,1,0], ' ':[1,1,1,1,1]}

    stringa = letturaStringa()  #carico la stringa

    if stringa == -1:   #se la scelta è sbagliata mostro un messaggio di errore ed interrompo il programma
        print("Scelta sbagliata")
        return

    lista = creaLista(stringa, dizionarioCaratteri) #creo la lista

    print(lista)    #stampo la lista

    #stampo la lista sul file
    stampaListaFile(lista)
        
    finestraPygame(lista)


if __name__ == "__main__":
    main()