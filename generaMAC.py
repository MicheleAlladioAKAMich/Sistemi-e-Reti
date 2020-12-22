"""
Author: Michele Alladio
es: generare un indirizzo MAC
"""
def main():

    def generaMac():
        import random, string   #importo le librerie

        #si definisce il formato del messaggio -> 2 caratteri:2 caratteri:2 caratteri:2 caratteri:........
        #successivamente si estraggono due caratteri random tra numeri e lettere maiuscole per 6 volte
        return "%02s:%02s:%02s:%02s:%02s:%02s" % (  
        random.choice(string.ascii_uppercase + string.digits) + random.choice(string.ascii_uppercase + string.digits),
        random.choice(string.ascii_uppercase + string.digits) + random.choice(string.ascii_uppercase + string.digits),
        random.choice(string.ascii_uppercase + string.digits) + random.choice(string.ascii_uppercase + string.digits),
        random.choice(string.ascii_uppercase + string.digits) + random.choice(string.ascii_uppercase + string.digits),
        random.choice(string.ascii_uppercase + string.digits) + random.choice(string.ascii_uppercase + string.digits),
        random.choice(string.ascii_uppercase + string.digits) + random.choice(string.ascii_uppercase + string.digits),
        )
    
    mac = generaMac()   #richiamo la funzione per generare l'indirizzo MAC
    print(mac)  #stampo l'indirizzo MAC

if __name__ == "__main__":
    main()  #richiamo il main