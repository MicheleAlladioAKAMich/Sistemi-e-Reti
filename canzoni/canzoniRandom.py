"""
Author: Michele Alladio
es: leggere delle canzoni da un file canzoni.csv e caricarle in una lista di dizionari
"""
def main():
    import random

    file = open("canzoni.csv", "r")  #apertura file  

    playlist = []

    for riga in file:
        lista = riga[:-1].split(",")
        playlist.append({"numero":lista[0],"titolo":lista[1],"autore":lista[2]})  #crea il dizionario di liste

    print(playlist)

    """listaRandom = playlist
    random.shuffle(listaRandom)

    for riga in listaRandom:
        print(riga)"""

    random.shuffle(playlist)    #randomizza l'ordine della playlist letta

    for riga in playlist:
        print(riga) #stampa ogni riga della playlist randomizzata


    file.close()    #chisura file

if __name__ == "__main__":
    main()