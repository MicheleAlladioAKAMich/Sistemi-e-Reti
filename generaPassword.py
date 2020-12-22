"""
Author: Michele Alladio
es: generare una password
"""
def main():

    def generaPassword(car):
        import random, string   #importo le lbrerie

        if car == "S":    
            #genera un carattere casuale scegliendo tra una carattere ascii maiuscolo, un carattere ascii minuscolo e 
            #un numero, il for alla fine della riga serve per far ripetere il tutto 8 volte
            password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for k in range(8))
        else:
            if car == "C":
                #genera un carattere casuale scegliendo tra una carattere ascii maiuscolo, un carattere ascii minuscolo e 
                #un numero, il for alla fine della riga serve per far ripetere il tutto 20 volte
                password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for k in range(20))
            else:
                #returna -1 (caso di errore)
                password = -1
        
        return password

    carattere = input("Inserisci S per una password semplice (8 caratteri) oppure C per una password complessa (20 caratteri): ")   #inserisco un carattere

    passw = generaPassword(carattere)    #richiamo la funzione

    if passw == -1: #se passw vale -1 allora si è verificato un errore
        print("Sceta sbagliata")
    else:   #altrimenti printo la password generata
        print(passw)

if __name__ == "__main__":
    main()  #richiamo il main