'''
Author: Michele Alladio
es: 
Detect palindrome products in a given range.
A palindromic number is a number that remains the same when its digits are reversed. For example, 121 is a palindromic number but 112 is not.
Given a range of numbers, find the largest and smallest palindromes which are products of numbers within that range.

EXAMPLE:
Given the range [10, 99] (both inclusive)...
The smallest palindrome product is 121. Its factors are (11, 11). The largest palindrome product is 9009. Its factors are (91, 99).
'''

def products(minFactor, maxFactor):
    internalNumbers = []    #lista dei numeri interni ai due fattori (inclusi)
    productsList = []   #lista di tutti i prodotti possibili tra i numeri interni
    #variabili per i prodotti palindromi
    minPalindrome = 0
    maxPalindrome = 0

    while minFactor <= maxFactor:   #inserimento dei numeri nella lista
        internalNumbers.append(minFactor)
        minFactor += 1
    
    #aggiornamento della lista dei prodotti
    for number1 in internalNumbers:
        for number2 in internalNumbers:
            if number1*number2 not in productsList: #controllo per escludere i duplicati
                productsList.append(number1*number2)
            
    #ricerca del minimo palindromo
    for number in productsList: #cicla la lista dei prodotti
        cntUnits = 0    #contatore per le unità in un numero
        
        for unit in str(number):    #individua il numero di unità in un numero (es: 9999 --> 4 unità)
            cntUnits += 1

        #in base al numero di unità il contatore viene ridimensionato per diventare la metà 
        if cntUnits % 2 != 0:
            cntUnits = int(cntUnits/2-0.5)  #ridimensionamento per difetto
        else:
            cntUnits = int(cntUnits/2)
        
        #ricerca del minimo palindromo
        if cntUnits == 0:
            minPalindrome = number
            break   #al primo numero individuato si interrompe la ricerca

        #controllo che prende la prima metà delle cifre nel numero 
        #e la confronta con la seconda metà ribaltata (es: 883388 --> 883 == 388 (ribaltato) --> 883 == 883)
        elif str(number)[cntUnits:] == str(number)[:-cntUnits][::-1]:   
            minPalindrome = number
            break   #al primo numero individuato si interrompe la ricerca

        

    
    #procedimento analogo per il massimo palindromo
    for number in productsList:
        cntUnits = 0

        for unit in str(number):
            cntUnits += 1
        
        if cntUnits % 2 != 0:
            cntUnits = int(cntUnits/2-0.5)
        else:
            cntUnits = int(cntUnits/2)

        if cntUnits == 0:
            maxPalindrome = number
        elif str(number)[cntUnits:] == str(number)[:-cntUnits][::-1]:
            maxPalindrome = number
            
    return minPalindrome, maxPalindrome


def main():
    minFactor = int(input("Inserisci il fattore più piccolo: "))
    maxFactor = int(input("Inserisci il fattore più grande: "))

    if minFactor > maxFactor:   #controllo 
        print("Errore nell'inserimento dei fattori")
        return
    else:
        print(f"Il minimo prodotto palindromo è: {products(minFactor,maxFactor)[0]} \nIl massimo prodotto palindromo è: {products(minFactor,maxFactor)[1]}")


if __name__ == "__main__":
    main()