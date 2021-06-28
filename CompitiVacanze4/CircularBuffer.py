'''
Author: Michele Alladio
es:
A circular buffer, cyclic buffer or ring buffer is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end.

A circular buffer first starts empty and of some predefined length. For example, this is a 7-element buffer:
[ ][ ][ ][ ][ ][ ][ ]

Assume that a 1 is written into the middle of the buffer (exact starting location does not matter in a circular buffer):
[ ][ ][ ][1][ ][ ][ ]

Then assume that two more elements are added — 2 & 3 — which get appended after the 1:
[ ][ ][ ][1][2][3][ ]

If two elements are then removed from the buffer, the oldest values inside the buffer are removed. The two elements removed, in this case, are 1 & 2, leaving the buffer with just a 3:
[ ][ ][ ][ ][ ][3][ ]

If the buffer has 7 elements then it is completely full:
[6][7][8][9][3][4][5]

When the buffer is full an error will be raised, alerting the client that further writes are blocked until a slot becomes free.

When the buffer is full, the client can opt to overwrite the oldest data with a forced write. In this case, two more elements — A & B — are added and they overwrite the 3 & 4:
[6][7][8][9][A][B][5]

3 & 4 have been replaced by A & B making 5 now the oldest data in the buffer. Finally, if two elements are removed then what would be returned is 5 & 6 yielding the buffer:
[ ][7][8][9][A][B][ ]

Because there is space available, if the client again uses overwrite to store C & D then the space where 5 & 6 were stored previously will be used not the location of 7 & 8. 7 is still the oldest element and the buffer is once again full.
[D][7][8][9][A][B][C]
'''

buffer = [' ', ' ', ' ', ' ', ' ', ' ', ' ']


def circularBuffer(character, first, currentPosition, spaceNumber):

    if first:   #se è il primo carattere
        if character == 'canc' or character == 'CANC':
            print("Il buffer è già vuoto")  #avviso 

        else:
            for space in buffer:
                spaceNumber += 1    #incremento capacità del buffer
            
            #posizionamento del primo carattere e calcolo della posizione corrente
            if spaceNumber % 2 == 0:    #se il numero di slot nel buffer è pari
                buffer[int(spaceNumber/2)] = character
                currentPosition = int(spaceNumber/2)
            else:    #se il numero di slot nel buffer è dispari
                spaceNumber -= 1
                buffer[int(spaceNumber/2)] = character
                currentPosition = int(spaceNumber/2)

    else:   #se non è il primo carattere
        if currentPosition == spaceNumber:  #se si è posizionati all'ultima cella del buffer
            currentPosition = 0 #si ritorna nella prima cella
        else:
            currentPosition += 1    #incremento della posizione

        full = True 
        empty = True
        #controllo degli elementi nel buffer
        for space in buffer:
            #se sono tutti spazi allora sarà empty, se sono tutti caratteri allora sarà full
            if space == ' ':
                full = False
            else:
                empty = False
        
        if character == 'canc' or character == 'CANC':  #comando per cancellare
                if empty:   #se il buffer è già vuoto
                    print("Il buffer è già vuoto")  #avviso
                    currentPosition -= 1
                else:
                    currentPosition -= 1 
                    buffer[currentPosition] = ' '   #cancellazione dell'ultimo carattere inserito
                    currentPosition -= 1
        elif full:  #se il buffer è pieno
            decision = input("Il buffer è pieno, scrivi si per sovrascrivere, qualsiasi altra risposta per mantenere il buffer attuale: ")  #avviso
            if decision == 'si' or decision == 'SI':
                buffer[currentPosition] = character #sovrascrittura del carattere
        else:
            buffer[currentPosition] = character #normale inserimento di un carattere

    print(buffer)

    return currentPosition, spaceNumber


def main():
    first = True    #controllo per dterminare se è il primo carattere inserito
    currentPosition = 0 #posizione nel buffer
    spaceNumber = 0 #capacità del buffer

    while True:
        number = 0  #numero di caratter inseriti
        character = input("Inserisci un carattere (ESC per uscire, CANC per cancellare l'ultimo elemento inserito): ")

        for element in character:
            number += 1
        if number > 1:  #se l'utente inserisce una parola al posto di un carattere
            if character == 'esc' or character == 'ESC':    #termina il programma
                break
            elif character == 'canc' or character == 'CANC':    #viene cancellato un elemento nel buffer
                currentPosition, spaceNumber = circularBuffer(character, first, currentPosition, spaceNumber)
                if not first:   #se canc è inserito come primo carattere non conta e first rimane a True
                    first = False
            else:   #altre parole
                print("Carattere non riconosciuto")

        else:   #se viene inserito un carattere
            currentPosition, spaceNumber = circularBuffer(character, first, currentPosition, spaceNumber)
            first = False   #il primo carattere è stato inserito
        
        
if __name__ == "__main__":
    main()