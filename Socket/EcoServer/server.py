'''
Author: Michele Alladio
es:'''

import socket as sck

def main():

    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM) #creo un socket UDP / IPv4
    s.bind(('127.0.0.1', 7000)) 

    while True:
        #recvfrom -> riceve e identifica il mittente (client)
        data, addr = s.recvfrom(4096)   #data = stringa ricevuta    addr -> tupla (IP client, porta client)
        s.sendto(data, addr)    #manda al client
        print(data)

if __name__ == "__main__":
    main()