'''
Author: Michele Alladio
es: 
The diamond kata takes as its input a letter, and outputs it in a diamond shape. 
Given a letter, it prints a diamond starting with 'A', with the supplied letter at the widest point.

Diamond for letter 'E':

····A····
···B·B···
··C···C··
·D·····D·
E·······E
·D·····D·
··C···C··
···B·B···
····A····

'''

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','']

def createDiamond(letter):
    character = 0   #carattere attuale dell'alfabeto
    externalPoints = 0  #contatore punti esterni alle lettere
    internalPoints = 0  #contatore punti interni alle lettere
    diamond = ''    #diamante

    #inizializzo il contatore di punti interni in base alla lettera inserita
    for element in alphabet:    
        if element == letter:
            break
        externalPoints+=1

    #PRIMA PARTE DEL DIAMANTE
    while alphabet[character-1] != letter:  #partendo dalla A fino alla lettera inserita

        for point in range(externalPoints):     #punti esterni
            diamond += '.'

        diamond += alphabet[character]  #prima lettera

        for point in range(internalPoints): #punti interni
            diamond += '.'
        
        if alphabet[character] != 'A':  #se la lettera non è la A stampo anche la seconda lettera
            diamond += alphabet[character]

        for point in range(externalPoints): #punti esterni
            diamond += '.'
        
        diamond += '\n' #a capo per la nuova linea

        character+=1    #si passa alla lettera successiva

        if alphabet[character] != 'B':  #controllo per il posizionamento corretto dei punti interni
            internalPoints+=2
        else:
            internalPoints+=1

        externalPoints-=1   #decremento del numero dei punti esterni

    #aggiusto il valore delle variabili prima di creare la seconda parte del diamante
    character = 0
    externalPoints = 0
    internalPoints-=2

    #operazione inversa, inizializzo il numero di caratteri per poi decrementarli fino alla A
    for element in alphabet:    
        if element == letter:
            break
        character+=1

    #SECONDA PARTE DEL DIAMANTE
    while alphabet[character+1] != 'A': #partendo dalla lettera inserita fino alla A

        for point in range(externalPoints): #punti esterni
            diamond += '.'

        diamond += alphabet[character]  #prima lettera

        for point in range(internalPoints): #punti interni
            diamond += '.'
        
        if alphabet[character] != 'A':  #se la lettera non è la A stampo anche la seconda lettera
            diamond += alphabet[character]

        for point in range(externalPoints): #punti esterni
            diamond += '.'
        
        diamond += '\n' #a capo per la nuova linea

        character-=1    #si passa alla lettera precedente
        internalPoints-=2   #decremento del numero di punti interni
        externalPoints+=1   #incremento del numero di punti esterni

    return diamond 



def main():
    letter = input("Inserisci una lettera: ").upper()   #prende l'input e lo trasforma in maiuscolo
    
    if letter not in alphabet:  #controlla che l'input corrisponda ad una lettera dell'alfabeto
        print("Non hai inserito una lettera dell'alfabeto")
    else:
        print(createDiamond(letter))    #crea il diamante

if __name__ == "__main__":
    main()