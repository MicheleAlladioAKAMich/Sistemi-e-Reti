"""
Author: Michele Alladio
es: generare una password semplice o complessa
"""
import random, string   #importo le lbrerie

def generaPassword(car):
    if car == "S":    
        #genera un carattere casuale scegliendo tra una carattere ascii maiuscolo/minuscolo e 
        #un numero, il for alla fine della riga serve per far ripetere il tutto 8 volte
        password = ''.join(random.choice(string.ascii_letters + string.digits) for k in range(8))
    else:
        if car == "C":
            #genera un carattere casuale scegliendo tra una carattere ascii maiuscolo/minuscolo e 
            #un numero, il for alla fine della riga serve per far ripetere il tutto 20 volte
            password = ''.join(random.choice(string.ascii_letters + string.digits) for k in range(20))
        else:
            #returna -1 (caso di errore)
            return -1
    
    return password

def main():
    carattere = input("Inserisci S per una password semplice (8 caratteri) oppure C per una password complessa (20 caratteri): ")   #inserisco un carattere

    passw = generaPassword(carattere)    #richiamo la funzione

    if passw == -1: #se passw vale -1 allora si è verificato un errore
        print("Scelta sbagliata")
    else:   #altrimenti printo la password generata
        print(passw)

if __name__ == "__main__":
    main()  #richiamo il main
