'''
Alladio Michele
Algoritmo di Dijkstra su un grafo predefinito definito da un dizionario
'''

'''
a 0
b 1
c 2
d 3
e 4
f 5
g 6
h 7
i 8
j 9
'''

dizionario = {
    0: [(3,4),(4,1),(7,10)],
    1: [(2,2),(5,1)],
    2: [(1,2),(5,3)],
    3: [(0,4),(7,1)],
    4: [(0,1),(7,5),(5,3)],
    5: [(1,1),(4,3),(6,7),(8,1),(2,3)],
    6: [(5,7),(9,1)],
    7: [(0,10),(3,1),(4,5),(8,9)],
    8: [(7,9),(5,1),(9,2)],
    9: [(6,1),(8,2)]
}

matrice = []

INFINITE = 99999999

def dijkstra(start, dizionario):
    dizLabel = {}
    nodeList = [start]  
    deletedList = []

    for node in dizionario:
        dizLabel[node] = INFINITE
    
    dizLabel[start] = 0

    while len(nodeList) > 0:
        currentLable = INFINITE
        #cerco tra i nodi presenti in nodelist quello che ha la label più piccola  
        #il nodo trovato sarà il nodo corrente
        for node in nodeList:
            if dizLabel[node] < currentLable:
                currentLable = dizLabel[node]
                currentNode = node

        nodeList.remove(currentNode)
        deletedList.append(currentNode)

        #trovo le adicenze a partire dal nodo corrente      
        for node, label in dizionario[currentNode]:
            if not(node in deletedList) and not(node in nodeList):
                nodeList.append(node)
            #per ogni adiacenza calcolo la nuova label aggiornando il dizionario label solo se la label trovata 
            #risulta più piccola di quella già trovata    
            if label + dizLabel[currentNode] < dizLabel[node]:
                dizLabel[node] = dizLabel[currentNode] + label
        
    return dizLabel

def main():
    start = int(input("Inserisci un nodo di partenza: "))
    #finish = input("Inserisci un nodo finale: ")

    control = False

    for node in dizionario:
        if start == node:
            control = True

    if control == False:
        print("Nodo non esistente")
    else:
        print(dijkstra(start,dizionario))

if __name__ == "__main__":
    main()
