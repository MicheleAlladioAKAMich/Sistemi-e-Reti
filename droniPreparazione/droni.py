'''
Author: Michele Alladio
'''

import sys, pygame, random, csv #librerie

def stampaLatLong(anomalie, volo):
    for anomalia in anomalie:   #ciclo le anomalie
        for elementi in volo:   #ciclo i tempi di volo
            if anomalia["Tempo"] == elementi["Tempo"]:  #se il tempo dell'anomalia coincide con il tempo di volo
                #print(f"TIPO DI ERRORE: {anomalia["Tipo"]} LATITUDINE ERRORE: {elementi["Latitudine"]} LONGITUDINE ERRORE: {elementi["Longitudine"]}")
                print("TIPO DI ERRORE: " + anomalia["Tipo"] + " LATITUDINE ERRORE: " + elementi["Latitudine"] + " LONGITUDINE ERRORE: " + elementi["Longitudine"])


def main():
    anomalie = []   #lista delle anomalie
    volo = []   #lista del volo

    #apertura file
    fileAnomalie = open("Anomalie_drone.csv", "r")
    fileVolo = open("Volo_drone.csv", "r")

    #lettura file e caricamento in una lista di dizionari
    for riga in fileAnomalie:
        lista = riga[:-1].split(",")
        anomalie.append({"Tempo": lista[0], "Tipo": lista[1]})
    
    for riga in fileVolo:
        lista = riga[:-1].split(",")
        volo.append({"Tempo": lista[0], "Latitudine": lista[1], "Longitudine": lista[2]})
    
    #stampa delle liste di dizionari
    print(anomalie)
    print(volo)

    stampaLatLong(anomalie, volo)   #stampa latitudine e longitudine

    #chiusura file
    fileAnomalie.close()
    fileVolo.close()

if __name__ == "__main__":
    main()