'''
Author: Michele Alladio
es:
'''

import socket as sck
import string
import threading as thr
import time

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  #creo un socket TCP / IPv4
    s.connect(('localhost', 7000))

    while True:
        message = input("Inserisci il messaggio: ")
        s.sendall(message.encode())

        data = s.recv(4096)
        print(data.decode())

if __name__ == "__main__":
    main()