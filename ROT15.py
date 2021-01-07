"""
Author: Michele Alladio
es: codifica e decodifica in ROT-15
"""

listaNormale = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'   #alfabeto
listaROT15 = 'PQRSTUVWXYZABCDEFGHIJKLMNOpqrstuvwxyzabcdefghijklmnop'    #alfabeto ROT-15

conversioneNormaleToROT15 = dict(zip(listaNormale, listaROT15)) #converte dall'alfabeto all'alfabeto ROT-15
conversioneROT15ToNormale = dict(zip(listaROT15, listaNormale)) #converte dall'alfabeto ROT-15 all'alfabeto 

def normaleToROT15(stringaEntrata): #conversione da alfabeto normale a ROT-15
    listaAppoggio = []  
    stringOutput = ''
    for lettera in stringaEntrata:  #fino a quando non si finisce la stringa
        if lettera in listaNormale: #se la lettera letta è presente nella lista dell'alfabeto
            listaAppoggio.append(conversioneNormaleToROT15[lettera])    #viene effettuata la conversione e la lettera convertita viene posta al fondo della lista di appoggio
        else:
            listaAppoggio.append(lettera)   #altrimenti non si effettua nessuna conversione es: numeri

    stringOutput = stringOutput.join(listaAppoggio) #il contenuto della lista di appoggio viene copiato nella stringa di output
    return stringOutput

def ROT15ToNormale(stringaEntrata): #conversione da ROT-15 ad alfabeto normale
    listaAppoggio = []
    stringOutput = ''
    for lettera in stringaEntrata:  #fino a quando non si finisce la stringa
        if lettera in listaNormale: #se la lettera letta è presente nella lista dell'alfabeto ROT-15
            listaAppoggio.append(conversioneROT15ToNormale[lettera])    #viene effettuata la conversione e la lettera convertita viene posta al fondo della lista di appoggio
        else:
            listaAppoggio.append(lettera)      #altrimenti non si effettua nessuna conversione es: numeri

    stringOutput = stringOutput.join(listaAppoggio) #il contenuto della lista di appoggio viene copiato nella stringa di output
    return stringOutput

def main():
    stringa = input("Inserisci una stringa (in alfabeto normale): ")
    print("ROT-15: " + normaleToROT15(stringa))
    print("ALFABETO NORMALE: " + ROT15ToNormale(normaleToROT15(stringa)))

if __name__ == "__main__":
    main()  #richiamo il main
