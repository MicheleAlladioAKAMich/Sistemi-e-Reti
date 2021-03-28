"""
Author: Michele Alladio
es: Il file annual.csv (allegato) contiene la anomalia della temperatura globale del pianeta Terra dal 1880 ad oggi, 
proveniente da varie fonti (colonna “Source”). 
Scrivere un programma che generi un dizionario che abbia come chiave l’anno (“Year”) e valore la media aritmetica delle
anomalie registrate dalle varie fonti durante quell’anno.
Inoltre scrivere una funzione che dati in input due anni diversi (anno_1 e anno_2) trovi la anomalia massima e minima 
nel periodo compreso tra anno_1 e anno_2.
"""

def trovaAnomalia(diz, primoAnno, secondoAnno):
    listaValori=[]    #lista delle medie contenute tra i due anni inseriti

    if primoAnno <= secondoAnno:    #se gli anni sono inseriti correttamente
        for scorriAnno in range(primoAnno, secondoAnno+1):  #si scorrono gli anni interessati
            listaValori.append(float(diz[str(scorriAnno)]))   #viene creata la lista delle medie usando il riferimento alla chiave del dizionario

        #stampa delle anomalie
        print("Anomalia massima: " + str(max(listaValori)))
        print("Anomalia minima: " + str(min(listaValori)))
    else:   #inserimento sbagliato degli anni
        print("INSERIRE PER PRIMO L'ANNO MINORE")

def main():
    fileRiscaldamento = open("annual.csv", "r").readlines()  #apertura file
  
    cntRighe = 0    #contatore per le righe
    temp = 0    #variabile di appoggio
    media = 0   #media
    cntProssimoAnno = 2 #serve per scorrere la riga successiva del file
    dizionario = {} #dizionario

    for riga in fileRiscaldamento[1:]:   #scorrimento file escludendo la prima riga
        
        annoSucc = fileRiscaldamento[cntProssimoAnno].split(",")    #in annoSuc viene caricata la riga successiva del file rispetto alla lettura effettuata dal for
        
        letturaRiga = riga[:-1].split(",")  #lettura riga
        cntRighe+=1 #incremento contatore delle righe
        temp = temp + float(letturaRiga[2]) #nella variabile di appoggio viene sommato il valore letto

        if float(annoSucc[1]) != float(letturaRiga[1]): #se l'anno successivo è diverso da quello attuale
            dizionario[letturaRiga[1]] = temp / cntRighe #dizionario{numero anno : media valori}
            temp = 0    #viene azzerata la variabile di appoggio
            cntRighe = 1    #il contatore delle righe viene ripristinato
                  
        if cntProssimoAnno < len(fileRiscaldamento)-1:  #se il contatore dell'anno successivo è minore della lunghezza del file -1
            cntProssimoAnno+=1  #viene incrementato
        else:
            cntProssimoAnno = 1 #viene ripristinato
    
    print(dizionario)   #stampa del dizionario

    #inserimento degli anni 
    anno1 = int(input("Inserisci il primo anno: "))
    anno2 = int(input("Inserisci il secondo anno: "))

    trovaAnomalia(dizionario, anno1, anno2) #trova anomalia massima e minima


if __name__ == "__main__":
    main()  #richiamo il main