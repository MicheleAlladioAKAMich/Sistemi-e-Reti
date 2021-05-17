'''
Author: Michele Alladio
es:
'''

import socket as sck
import string
import threading as thr
import time

class Receive_message(thr.Thread):
    def __init__(self, s):
        thr.Thread.__init__(self)   #costruttore super (java) 
        self.running = True
        self.s = s

    def run(self):
        while self.running:
            data = self.s.recv(4096)
            print(data.decode())
            '''if data.decode().startswith('exit'):
                self.running = False'''

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)  #creo un socket TCP / IPv4
    s.connect(('localhost', 7000))

    nickname = input("Inserisci un nickname: ")
    s.sendall(nickname.encode())
    print("Connessione avvenuta")

    #Thread per la ricezione dei messaggi
    receiver = Receive_message(s)
    receiver.start()

    while True:
        message = input("Inserisci il messaggio: ")
        s.sendall(message.encode())

        '''data = s.recv(4096)
        print(data.decode())'''

        '''if receiver.running == False:
            print("Chiusura")
            receiver.join()'''

    s.close()

if __name__ == "__main__":
    main()