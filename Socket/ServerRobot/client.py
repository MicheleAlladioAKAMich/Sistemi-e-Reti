'''
Author: Michele Alladio
es:'''

import socket as sck
import string

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)  #creo un socket UDP / IPv4
    print("COMANDARE IL ROBOT\nW per salire\nS per scndere\nA per andare a sinistra\nD per andare a destra\nexit per uscire")

    '''stringa = print("Inserisci una stringa: ")
    nuovaStringa = stringa'''

    while True:
        message = input()
        byte = str.encode(message)
        s.sendto(byte, ('localhost', 7000))

if __name__ == "__main__":
    main()