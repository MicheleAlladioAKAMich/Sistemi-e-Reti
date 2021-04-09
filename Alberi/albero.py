'''
Author: Michele Alladio
es:
Gestione generale di un albero
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
            
    def printTree(self):    #stampa ricorsiva di tutti i valori da sx verso dx
        if self.left:
            self.left.printTree()

        print(self.data)
        
        if self.right:
            self.right.printTree()

    #attraversamento in ordine
    def inOrderTraversal(self, root):
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res

    #attraversamento pre-ordine
    def preorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorderTraversal(root.left)
            res = res + self.preorderTraversal(root.right)
        return res
    
    #attraversamento post-ordine
    def postorderTraversal(self, root):
        res = []
        if root:
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res


root = Node(27) #12 è la radice
#inserimento dei rami/foglie
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

root.printTree()    #stampa
print(root.inOrderTraversal(root))
print(root.preorderTraversal(root))
print(root.postorderTraversal(root))
