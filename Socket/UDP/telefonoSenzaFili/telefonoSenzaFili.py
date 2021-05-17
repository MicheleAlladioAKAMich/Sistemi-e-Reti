'''
Author: Michele Alladio
es:
realizzare un programma che prenda legga un messaggio in arrivo da un terminale e lo ripeta su di un terminale successivo
'''

import socket as sck
import string

def main():

    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM) #creo un socket UDP / IPv4
    s.bind(('192.168.0.131', 7000)) 
    
    while True:
        data, addr = s.recvfrom(4096)   #data = stringa ricevuta    addr -> tupla (IP client, porta client)
        print(data.decode())
        s.sendto(data, ('192.168.0.127', 7000))    #manda al client successivo

if __name__ == "__main__":
    main()