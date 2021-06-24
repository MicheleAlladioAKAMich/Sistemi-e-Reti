'''
Author: Michele Alladio
es: 
Given a number, find the sum of all the unique multiples of particular numbers up to but not including that number.
If we list all the natural numbers below 20 that are multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.
The sum of these multiples is 78.
'''

def calculateNumber(number, n1, n2):
    cnt = 1 #contatore
    multiple = 0  
    total = 0
    numberList = [] #lista dei multipli già presenti (che non vanno ripetuti)

    while multiple + n1 < number: #se il prossimo multiplo non supera il numero soglia
        multiple = n1*cnt     #aggiornamento del multiplo raggiunto 
        cnt+=1
        total += multiple #aggiornamento del totale (somma dei multipli)
        numberList.append(multiple) #il multiplo viene aggiunto alla lista di quelli già presenti
    
    #re-dichiarazione del multiplo e del contatore
    multiple = 0
    cnt = 1

    while multiple + n2 < number: #se il prossimo risultato non supera il numero soglia
        multiple = n2*cnt     #aggiornamento del risultato raggiunto
        cnt+=1
        if multiple not in numberList:  #controllo per prevenire il conteggio di doppi multipli
            total += multiple
    
    return total

def main():
    number = int(input("Inserisci il numero da non superare: "))
    if number <= 0: #primo controllo
        print("Numero da non superare troppo piccolo.")
    else:
        n1 = int(input("Inserisci il primo numero: "))
        n2 = int(input("Inserisci il secondo numero: "))

        if n1 >= number or n2 >= number:    #secondo controllo
            print("I numeri inseriti devono essere minori del numero da non superare")
        else:
            print(f"Somma dei multipli: {calculateNumber(number, n1, n2)}") #calcolo e stampa della somma

if __name__ == "__main__":
    main()