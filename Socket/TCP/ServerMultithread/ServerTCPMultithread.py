import socket as sck
import threading as thr

clientList = []

class Client_Manager(thr.Thread):
    def __init__(self, connection, nickname):
        thr.Thread.__init__(self)   #costruttore super (java)
        self.connection = connection
        self.nickname = nickname
        self.running = True
    
    def run(self):
        while self.running:
            receivedMessage = self.connection.recv(4096)

            if receivedMessage.decode().startswith('exit'): #se il messaggio ricevuto inizia con exit viene chiuso il client
                self.running = False
            else:
                print(f"Messaggio ricevuto da [{self.nickname.decode()}]: {receivedMessage.decode()}")

            receiver = input("Inserisci un destinatario: ")

            #controllo del destinatario
            if receiver == 'all':   #all -> manda a tutti i client
                for client in clientList:
                    client.connection.sendall(receivedMessage) 
            else:
                for client in clientList:
                    if client.nickname.decode() == receiver:
                        client.connection.sendall(receivedMessage) 


def main():
    print(f"Io sono {thr.current_thread()}")
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.bind(("127.0.0.1", 7000))
    s.listen()

    global clientList

    dizUsers = {}

    while True:
        connection, address = s.accept()

        #Ricezione del nickname
        nickname = connection.recv(4096)
        dizUsers[nickname.decode()] = address
        print(dizUsers)

        #creazione del thread -> uno per ogni client
        client = Client_Manager(connection, nickname)
        clientList.append(client)
        client.start()

        #chiusura del client
        for client in clientList:   
            if not client.running:
                print("Chiusura")
                client.connection.close()
                client.join()  
                clientList.remove(client)   

if __name__ == "__main__":
    main()