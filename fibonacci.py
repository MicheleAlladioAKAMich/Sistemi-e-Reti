"""
Author: Michele Alladio
es: serie di fibonacci entro una soglia impostata dall'utente
"""
def fibonacciRicorsiva(num, k, primoN, secondoN, som): 
    if num <= 0: print("non serve a molto :)")     #caso -> soglia = 0  
    else:
        if num == 1: print(primoN) #caso -> soglia = 1
        else:    #caso -> soglia > 1
            if k < 2:   #la prima volta che entra
                print(primoN)   #printa il primo numero -> 1
                print(secondoN)   #printa il secondo numero -> 1
                k = 2   #forza il contatore a 2
                fibonacciRicorsiva(num, k, primoN, secondoN, som)   #richiama la funzione ricorsiva
            else:
                if k < num: #fino a quando il contatore è minore della soglia
                    k += 1  #aggiorna il valore del contatore

                    som = primoN + secondoN  #calcola la somma
                    print(som)  #stampa la somma

                    primoN = secondoN  #aggiorna il valore del primo numero
                    secondoN = som  #aggiorna il valore del secondo numero

                    fibonacciRicorsiva(num, k, primoN, secondoN, som)   #richiama la funzione ricorsiva

def main():
    #inizializzo le varibili che mi servono
    cnt = 0
    primoNumero = 1 
    secondoNumero = 1
    somma = 0

    soglia = int(input("Inserisci una soglia: "))   #inserisco castando ad int la soglia
    fibonacciRicorsiva(soglia, cnt, primoNumero, secondoNumero, somma)  #richiamo la funzione ricorsiva


if __name__ == "__main__":
    main()  #richiamo il main
