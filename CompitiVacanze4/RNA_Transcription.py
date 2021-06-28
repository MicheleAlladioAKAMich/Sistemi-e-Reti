'''
Author: Michele Alladio
es:
Given a DNA strand, return its RNA complement (per RNA transcription).

Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

G -> C
C -> G
T -> A
A -> U
'''

DNA_List = ['A', 'C', 'G', 'T']
RNA_List = ['U', 'G', 'C', 'A']

def createRNA(dna):
    rna = ''

    #creazione della lista
    for letter in dna:
        position = -1   #posizione nella lista DNA
        for nucleotide in DNA_List:
            position += 1   #incremento della posizione
            if letter == nucleotide:    #confronto tra le lettere della stringa ricevuta ed i nucleotidi nella lista del DNA
                rna += RNA_List[position] #passaggio da DNA ad RNA
    
    return rna

def main():
    dna = input("Inserisci un DNA (il DNA è composto dalle lettere G, C, T, A): ").upper()

    for letter in dna:
        if letter not in DNA_List:   #controllo compatibilità dei caratteri nella stringa con i nucleotidi del DNA
            print("Formato del DNA sbagliato!")
            return
        
    print(f"Ecco il tuo RNA: {createRNA(dna)}")


if __name__ == "__main__":
    main()
    