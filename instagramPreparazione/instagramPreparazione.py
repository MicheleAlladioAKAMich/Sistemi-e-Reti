'''
Author: Michele Alladio
'''

import sys, pygame, random, csv #librerie

def main():
    instagram = []   #lista

    #apertura file
    fileInstagram = open("instagram.csv", "r")

    #lettura file e caricamento in una lista di dizionari
    cntRiga = 0

    for riga in fileInstagram:  #carico il file in una lista di dizionari
        if cntRiga != 0:    #salto la prima riga
            lista = riga[:-1].split(",")
            instagram.append({"Mese": lista[0], "Giorno": lista[1], "ID_post": lista[2], "Like": lista[3]})
        
        cntRiga = 1
    
    #print(instagram)

    listaMesi = ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"]

    dizionario = {} #dizionario dei mesi

    for mese in listaMesi:
        sommaLike = 0
        for riga in instagram:
            if riga["Mese"] == mese:
                sommaLike += int(riga["Like"])
        
        dizionario[mese] = sommaLike

    print(dizionario)

    stringa = input("Dammi un mese: ")  #inserisco un mese come stringa

    trovato = False

    for mese, numero in dizionario.items(): #se il mese corrisponde ad un mese nel dizionario stampo i like corrispondenti
        if(stringa == mese):
            print(numero)
            trovato = True
    
    if trovato == False:
        print("Non esiste questo mese")

    
if __name__ == "__main__":
    main()