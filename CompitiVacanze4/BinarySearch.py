'''
Author: Michele Alladio
es: 
Given a phrase, count the occurrences of each word in that phrase.
'''

alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L',
            'M','N','O','P','Q','R','S','T','U','V','W','X',
            'Y','Z','0','1','2','3','4','5','6','7','8','9']

dizWords = {}

def wordsCounter(string):
    
    for world in string:    #per ogni parola
        if world[-1].upper() not in alphabet:   #se l'ultimo carattere maiuscolo della parola non è nell'alfabeto viene omesso
            world = world[:-1]
        
        if world not in dizWords:   #se la parola non è nel dizionario
            dizWords[world] = 1 #viene inserita con valore pari a 1
        else:   #se è già presente
            dizWords[world] += 1    #il suo valore viene incrementato

    return dizWords

def main():
    string = input("Inserisci una stringa: ")

    print(wordsCounter(string.split(" ")))  #alla funzione viene passata la stringa splittata

if __name__ == "__main__":
    main()