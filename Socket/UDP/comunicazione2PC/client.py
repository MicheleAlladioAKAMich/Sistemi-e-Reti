'''
Author: Michele Alladio
es:'''

import socket as sck, string
buffer = 4096   #numero massimo di informazioni traslabili

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)  #creo un socket UDP / IPv4

    '''stringa = print("Inserisci una stringa: ")
    nuovaStringa = stringa'''

    '''while True:
        s.sendto(b'ciao', ('192.168.12.1', 22222))
        data, addr = s.recvfrom(4096)'''

    while True:
        message = input("Inserisci una stringa: ")
        byte = str.encode(message)
        s.sendto(byte, ('192.168.12.1', 22222))

        returnMessage = s.recvfrom(buffer)

        messagePrint = "Message from server {}".format(returnMessage[0])    #stampa il messaggio che l'altro server ha mandato come risposta

        print(messagePrint)

if __name__ == "__main__":
    main()


