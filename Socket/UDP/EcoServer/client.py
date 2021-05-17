'''
Author: Michele Alladio
es:'''

import socket as sck
import string

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)  #creo un socket UDP / IPv4

    '''stringa = print("Inserisci una stringa: ")
    nuovaStringa = stringa'''

    while True:
        s.sendto(b'ciao', ('localhost', 7000))
        data, addr = s.recvfrom(4096)

if __name__ == "__main__":
    main()