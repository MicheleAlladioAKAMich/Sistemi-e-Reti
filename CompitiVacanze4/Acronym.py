'''
Author: Michele Alladio
es: 
Convert a phrase to its acronym.
Techies love their TLA (Three Letter Acronyms)!
'''

def createAcronym(phrase):
    acronym = phrase[0].upper() #prima lettera della frase maiuscola

    for letter in range(1, len(phrase)):
        if phrase[letter-1] == ' ': #ogni lettera che prima abbia uno spazio
            acronym += phrase[letter].upper()   #aggiornamento dell'acronimo con la corrispondente lettera maiuscola
    
    return acronym

def main():
    phrase = input("Inserisci una stringa: ")

    print(f"Acronimo di {phrase}: {createAcronym(phrase)}")    #crea l'acronimo

if __name__ == "__main__":
    main()