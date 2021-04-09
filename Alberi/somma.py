'''
Author: Michele Alladio
es:
Dato un albero etichettato con numeri naturali, scrivere una funzione
somma(a) che restituisca la somma di tutti i valori con cui sono
etichettati i nodi dell'albero.
'''

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data): #ricorsiva
        #confronta il valore del nodo da aggiungere con il nodo corrente
        if self.data:    #se esiste
            if data < self.data:
                if self.left is None:   #se arriviamo su una foglia crea il nodo
                    self.left = Node(data)
                else:
                    self.left.insert(data)  #continua la ricerca 
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    #attraversamento in ordine
    def inOrderTraversal(self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res

    def sumNode(self):
        somma = 0
        lista = root.inOrderTraversal(self) #lettura dei valori dell'albero
        for numero in lista:    #aggiornamento della somma seguendo la lista di valori ricavata
            somma += numero
        return somma


root = Node(27) #12 è la radice
#inserimento dei rami/foglie
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

#somma
somma = root.sumNode()
print(somma)