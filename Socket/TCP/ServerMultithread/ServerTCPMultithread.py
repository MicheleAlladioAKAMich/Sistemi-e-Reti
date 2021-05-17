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

            print(f"<{thr.current_thread()}> Messaggio ricevuto da {self.nickname.decode()}: {receivedMessage.decode()}")

            for thread in clientList:
                thread.connection.sendall(receivedMessage) 

            if receivedMessage.decode().startswith('exit'):
                self.running = False
                self.connection.close()   


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

        client = Client_Manager(connection, nickname)
        clientList.append(client)
        client.start()

        for client in clientList:
            if client.running == False:
                print("Chiusura")
                client.join()       

if __name__ == "__main__":
    main()